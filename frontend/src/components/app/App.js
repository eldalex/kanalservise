import './App.css';
import Graph from "../appGraph/Graph";
import TotalCost from "../appTotalCost/TotalCost";
import CurrentTable from "../appCurrentTable/CurrentTable";

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
