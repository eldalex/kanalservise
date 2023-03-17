import './App.css';
import Graph from "../appGraph/Graph";
import TotalCost from "../appTotalCost/TotalCost";
import CurrentTable from "../appCurrentTable/CurrentTable";

// App Состоит из:
// <Graph/> - сами графики, два штуки, по сути одинаковые. просто в разной валюте.
// <TotalCost/> - компонент общей стоимости
// <CurrentTable/> - компонент текущих рабочих данных

function App() {

    return (
        <div className="App, container-fluid">
            <div className="row">
                <div className="col-8">
                    <Graph/>
                </div>
                <div className="col">
                    <TotalCost/>
                    <CurrentTable/>
                </div>
            </div>
        </div>
    );
}

export default App;
