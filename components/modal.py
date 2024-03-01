import streamlit as st
from streamlit_modal import Modal


modal_create_master = Modal("Create Master", key="create_master_modal")
modal_create_eds = Modal("Create EDS Plan", key="create_eds_modal")
modal_load_master = Modal("Load Master", key="load_master_modal")
modal_load_eds = Modal("Load EDS Plan", key="load_eds_modal")
modal_save_master = Modal("Save Master", key="save_master_modal")
modal_save_eds = Modal("Save EDS Plan", key="save_eds_modal")