import React from 'react';
import './Header.css';

function Header() {
    return (
        <header className='header'>
            <div className="logo">
                <svg xmlns="http://www.w3.org/2000/svg" className="icon icon-tabler icon-tabler-compass" width="36" height="36" viewBox="0 0 24 24" strokeWidth="1.5" stroke="#f26a2e" fill="none" strokeLinecap="round" strokeLinejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <path d="M8 16l2 -6l6 -2l-2 6l-6 2" />
                    <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
                    <path d="M12 3l0 2" />
                    <path d="M12 19l0 2" />
                    <path d="M3 12l2 0" />
                    <path d="M19 12l2 0" />
                </svg>
                <h3>eCompass</h3>
            </div>

            <div className="createAccountButtons">
                <HeaderButton name="Log In" href="#"/>
                <HeaderButton name="Sign Up" href="#"/>
            </div>
        </header>
    )
}

function HeaderButton(props) {
    return (
        <a href={props.href}>
            <button>
                {props.name}
            </button>
        </a>
    )
}

export default Header;
