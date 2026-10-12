
function updateTask(index) {
    const updated = prompt("Enter updated task:", tasks[index]);

    if (updated === null) {
        return;
    }

    if (updated.trim() === "") {
        alert("Task cannot be empty!");
        return;
    }

    tasks[index] = updated.trim();

    localStorage.setItem("myTasks", JSON.stringify(tasks));

    displayTasks();

    alert("Task updated successfully!");
}
