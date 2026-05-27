
import time
from PageObj.login import Login


def test_list_hand_tools(context, capsys) -> None:
    login = Login(context)
    page = login.login()
    page.get_by_text(" Categories ").click()
    page.get_by_role("link", name= "Hand Tools").click()
    time.sleep(10)

    final_list = []
    number_of_pages = page.locator(".page-item").count() - 2
    print(number_of_pages)
    container = page.locator(".card-title").all()
    while number_of_pages != 0:
        print("I was here")
        temp_list = []

        for c in container:
            if c:
                temp_list.append(c.inner_text())
            else:
                break
        final_list = final_list + temp_list
        next_button = page.locator(".page-item").filter(has_text="»")
        next_button.click()
        time.sleep(4)
        container = page.locator(".card-title").all()
        number_of_pages = number_of_pages -1

    with capsys.disabled():
        print(final_list)



def test_page_table(context, capsys) -> None:
    login = Login(context)
    page = login.login()
    with page.expect_popup() as popup:
        page.get_by_text("Documentation").click()

    child_page = popup.value
    time.sleep(5)
    tech_list = []
    target_table = child_page.locator("table").filter(has_text="Technology")
    rows =  target_table.locator("tr").all()
    for row in rows:
        cells= row.locator("td").nth(1).all()
        for cell in cells:
            tech_list.append(cell.inner_text())
    with capsys.disabled():
        print(tech_list)





