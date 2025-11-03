from datetime import datetime


class WebPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.published_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def display(self):
        print("-" * 50)
        print(f"Заголовок: {self.title}")
        print(f"Опубликовано: {self.published_at}")
        print("Содержимое:")
        print(self.content if self.content.strip() else "(пусто)")
        print("-" * 50)


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)
        print(f"Страница «{page.title}» добавлена.")

    def remove_page_by_index(self, idx):
        if 0 <= idx < len(self.pages):
            removed = self.pages.pop(idx)
            print(f"Страница «{removed.title}» удалена.")
        else:
            print("Нет страницы с таким номером.")

    def display_info(self):
        print("=" * 50)
        print(f"Сайт: {self.name}")
        print(f"URL:  {self.url}")
        print(f"Всего страниц: {len(self.pages)}")
        if not self.pages:
            print("Страниц пока нет.")
        else:
            print("Список страниц:")
            for i, p in enumerate(self.pages):
                print(f"{i}. {p.title} ({p.published_at})")
        print("=" * 50)


def main():
    site = None

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Создать сайт")
        print("2. Показать информацию о сайте")
        print("3. Добавить страницу")
        print("4. Удалить страницу (по номеру)")
        print("5. Открыть страницу (показать содержимое)")
        print("0. Выйти")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            name = input("Название сайта: ").strip()
            url = input("URL: ").strip()
            if not name or not url:
                print("Название и URL не должны быть пустыми.")
                continue
            site = WebSite(name, url)
            print("Сайт создан.")

        elif choice == "2":
            if site is None:
                print("Сайт ещё не создан.")
            else:
                site.display_info()

        elif choice == "3":
            if site is None:
                print("Сначала создайте сайт.")
                continue
            title = input("Заголовок страницы: ").strip()
            content = input("Текст страницы: ")
            page = WebPage(title, content)
            site.add_page(page)

        elif choice == "4":
            if site is None:
                print("Сначала создайте сайт.")
                continue
            if not site.pages:
                print("Удалять нечего — страниц нет.")
                continue
            site.display_info()
            num = input("Введите номер страницы для удаления: ").strip()
            if not num.isdigit():
                print("Нужно ввести число.")
                continue
            site.remove_page_by_index(int(num))

        elif choice == "5":
            if site is None:
                print("Сначала создайте сайт.")
                continue
            if not site.pages:
                print("Страниц нет.")
                continue
            site.display_info()
            num = input("Введите номер страницы для открытия: ").strip()
            if not num.isdigit():
                print("Нужно ввести число.")
                continue
            idx = int(num)
            if 0 <= idx < len(site.pages):
                site.pages[idx].display()
            else:
                print("Нет страницы с таким номером.")

        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
