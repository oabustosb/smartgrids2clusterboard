import os
from typing import Callable, Tuple

import streamlit as st

from auth.session import SessionState

ENV_TOKENS = ["PUBLIC", "XM", "CEO", "CELSIA", "CODENSA", "CENS"]

def is_authenticated(pwd: str) -> bool:
    return pwd in [
            os.environ[token]
            for token in ENV_TOKENS
            ]

def login(blocks: Tuple) -> str:
    style, element = blocks
    style.markdown("""
    <style>
        input { -webkit-text-security: disc; }
    </style>
    """, unsafe_allow_html=True)
    return element.text_input("Por favor ingrese el token de acceso:")


def clean_blocks(*blocks):
    for block in blocks:
        block.empty()

def with_password(session_state: SessionState):
    if session_state["password"]:
        login_blocks = None
        password = session_state["password"]
    else:
        login_blocks = st.empty(), st.empty()
        password = login(login_blocks)
        session_state["password"] = password

    def wrapper(entry_point: Callable):

        def wrapped():
            if is_authenticated(password):
                if login_blocks is not None:
                    clean_blocks(*login_blocks)
                entry_point()
            elif password:
                st.error("Token incorrecto.")
        return wrapped
    return wrapper

def validate_access(select_results, session_state) -> bool:
    if select_results.vendor is None:
        return True
    if session_state.password != os.environ[select_results.vendor.upper()]:
        return False
    return True
