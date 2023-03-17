import {useSelector} from "react-redux";
import './totalcost.css'
const TotalCost = () => {
    const {totalCostInDollars, totalCostInRubles} = useSelector(state => state)
    return (
        <div className="total-cost">
            <table className="table">
                <thead className='table-dark'>
                <tr>
                    <th colSpan="2">Total</th>
                </tr>
                <tr>
                    <th>Cost in Dollars</th>
                    <th>Cost in Rubles</th>
                </tr>
                </thead>
                <tbody>
                <tr className="table-info">
                    <td>{totalCostInDollars}</td>
                    <td>{totalCostInRubles}</td>
                </tr>
                </tbody>
            </table>
        </div>
    )
}

export default TotalCost