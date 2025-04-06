import streamlit as st

st.title("📝 To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task:")
if st.button("Add Task") and new_task:
    st.session_state.tasks.append({"task": new_task, "status": "Not Started", "notes": ""})
    st.success("Task added!")
for idx, task in enumerate(st.session_state.tasks):
    cols = st.columns([4, 2, 3])
    with cols[0]:
        st.text_input("Task", value=task["task"], key=f"task_{idx}")
    with cols[1]:
        st.selectbox("Status", ["Not Started", "In Progress", "Done"], index=["Not Started", "In Progress", "Done"].index(task["status"]), key=f"status_{idx}")
    with cols[2]:
        st.text_area("Notes", value=task["notes"], key=f"notes_{idx}")
done = sum(1 for i in range(len(st.session_state.tasks)) if st.session_state[f"status_{i}"] == "Done")
total = len(st.session_state.tasks)
st.progress(done / total if total else 0)
st.write(f"✅ {done}/{total} tasks completed")
if st.button("Clear All Tasks"):
    st.session_state.tasks = []

