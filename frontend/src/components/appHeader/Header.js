import './header.css'
import logo from "../../img/logo.png"

const Header = () => {
    return (
        <div className="header-dash">
            <div className="logo">
                <img
                    src={logo}
                    width="200"
                    className="img-thumbnail"
                    alt="logo"
                />
            </div>
            <hr/>
            <span className="header-text">
                <h1>Му super dashboard for Kanalservice</h1>
            </span>
        </div>)
}

export default Header;