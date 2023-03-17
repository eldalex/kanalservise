import {useSelector} from "react-redux";

const CurrentTable = () => {
    const {currentTable} = useSelector(state => state)
    return (
        <div className="current-table">
            <table className="table">
                <thead className='table-dark'>
                <tr>
                    <th>id</th>
                    <th>№ Заказа</th>
                    <th>Стоимость в $</th>
                    <th>Дата доставки</th>
                    <th>Стоимость в ₽</th>
                </tr>
                </thead>
                <tbody>
                { !currentTable || currentTable.length <=0 ?(
                    <tr>
                        <td colSpan="4" align="center">
                            <b>Похоче что данных нет</b>
                        </td>
                    </tr>
                ):
                currentTable.map((order,index)=>(
                    <tr key={index} className="table-info">
                        <td>{index}</td>
                        <td>{order.order_number}</td>
                        <td>{order.order_cost_in_dollars}</td>
                        <td>{order.delivery_time}</td>
                        <td>{order.order_cost_in_rubles}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    )
}

export default CurrentTable