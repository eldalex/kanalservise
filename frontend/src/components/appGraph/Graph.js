import React, {useEffect} from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
import {useDispatch, useSelector} from "react-redux";
import axios from "axios";
import {API_URL} from "../../index";
import {setTable, setTotalCostInDollars, setTotalCostInRubles} from "../../actions";
import {Button} from "reactstrap";

const Graph = () => {
    const {currentTable} = useSelector(state => state)
    const dispatch = useDispatch()
    const reloadGrahp = () => {
        axios.get(API_URL)
            .then(data => sortBy(data.data))
    }

    const totalCostCalculation = (data) => {
        let totalinDollars=0, totalinRubles=0
        data.forEach((order)=>{
            totalinDollars+=order.order_cost_in_dollars
            totalinRubles+=order.order_cost_in_rubles
        })
        dispatch(setTotalCostInDollars(totalinDollars))
        dispatch(setTotalCostInRubles(Math.round(totalinRubles * 100) / 100))
    }

    const sortBy = (data) => {
        const sortedData = [...data].sort((a, b) => a["delivery_time"].localeCompare(b["delivery_time"]));
        dispatch(setTable(sortedData))
        totalCostCalculation(sortedData)
    };

    useEffect(() => {
        reloadGrahp()
        setInterval(() => {
            reloadGrahp();
        }, 600000);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])
    return (
        <>
            <div className="test">
                <LineChart width={1200} height={350} data={currentTable}>
                    <CartesianGrid strokeDasharray="3 3"/>
                    <XAxis dataKey="delivery_time"/>
                    <YAxis/>
                    <Tooltip/>
                    <Legend/>
                    <Line type="monotone" dataKey="order_cost_in_dollars" stroke="#8884d8" activeDot={{r: 8}}/>
                </LineChart>
            </div>
            <LineChart width={1200} height={350} data={currentTable}>
                <CartesianGrid strokeDasharray="3 3"/>
                <XAxis dataKey="delivery_time"/>
                <YAxis/>
                <Tooltip/>
                <Legend/>
                <Line type="monotone" dataKey="order_cost_in_rubles" stroke="#8884d8" activeDot={{r: 5}}/>
            </LineChart>
            <Button onClick={reloadGrahp}>Обновить</Button>
        </>
    );
};

export default Graph;
