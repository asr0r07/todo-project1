from django.shortcuts import render
from django.http import HttpResponse


def task_list(request):
    if request.method == 'POST':
        task_name = request.POST.get('taskName')
        description = request.POST.get('description')
        due_date = request.POST.get('dueDate')
        priority = request.POST.get('priority')

        # Ma'lumotlarni saqlash yoki boshqa amallarni bajarish

        # Xabar yuborish (masalan, muvaffaqiyatli saqlash)
        return HttpResponse("Vazifa muvaffaqiyatli saqlandi!")

    html_response = """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yangi Vazifa Yaratish</title>
    </head>
    <body>

        <h2>Yangi Vazifa Yaratish</h2>

        <form action="" method="post">
            <label for="taskName">Vazifa nomi:</label><br>
            <input type="text" id="taskName" name="taskName" required><br><br>

            <label for="description">Tavsif:</label><br>
            <textarea id="description" name="description" rows="4" cols="50" required></textarea><br><br>

            <label for="dueDate">Oxirgi sana:</label><br>
            <input type="date" id="dueDate" name="dueDate" required><br><br>

            <label for="priority">Muhimlik darajasi:</label><br>
            <select id="priority" name="priority" required>
                <option value="past">O'tgan</option>
                <option value="medium">O'rta</option>
                <option value="high">Yuqori</option>
            </select><br><br>

            <button type="submit">Hammasini_Saqlash</button>
        </form>

    </body>
    </html>
    """
    return HttpResponse(html_response)
