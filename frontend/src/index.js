import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reducer from "./reducer"
import App from './components/app/App';
import {createStore} from "redux";
import {Provider} from "react-redux";
import Header from "./components/appHeader/Header";
import 'bootstrap/dist/css/bootstrap.min.css'

// Адрес API с которого забираем наши данные
export const API_URL = "http://192.168.56.101:8888/api/table/"

// Будем использовать redux
const strore = createStore(reducer)

// Header - компонент заголовок (шапка)
// App - всё остальное

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={strore}>
        <Header/>
        <App/>
    </Provider>
);
