import time

# Browser history
# Доп.задания: 3 ; 5

class HistoryNode:
    def __init__(self, url, flagged):
        self.url = url
        self.flagged = flagged
        self.time_raw = time.time()
        self.time_clear = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.time_raw))
        self.domain = self.get_domain(url)
        self.prev = None  
        self.next = None 

    def get_domain(self, url):
        url = url.replace('https://', '').replace('http://', '').replace('www.', '')
        return url.split('/')[0]

class BrowserHistory:
    def __init__(self):
        self.head = None     
        self.tail = None      
        self.current = None   

    def add_page(self, url, flagged=False):
        new_page = HistoryNode(url, flagged)
        
        if not self.head:
            self.head = self.tail = self.current = new_page
        else:
            new_page.prev = self.current
            self.current.next = new_page
            self.tail = new_page
            self.current = new_page

    def clear_history(self):
        self.head = None
        self.tail = None
        self.current = None
        print("История браузера очищена")

    def navigation_forward(self):
        if not self.current:
            print("Нету истории браузера")
            return None
        else:
            if self.current.next:
                self.current = self.current.next
                print("Навигация вперёд")
                return self.current.url
            else:
                print("Навигация вперёд невозможна")
                return None

    def navigation_backward(self):
        if not self.current:
            print("Нету истории браузера")
            return None
        else:
            if self.current.prev:
                self.current = self.current.prev
                print("Навигация назад")
                return self.current.url
            else:
                print("Навигация назад невозможна")
                return None

    def domain_search(self, searched_domain):
        if not self.head:
            print("Нету истории браузера")
            return []

        results = []
        current = self.head

        while current:
            if searched_domain.lower() in current.domain.lower():
                results.append(current)
            current = current.next

        if results:
            print("Искомый домен:", searched_domain)
            print("Было найдено:", len(results), "\n")
            for found_pages in results:
                if found_pages.flagged:
                    flag = "★"
                else:
                    flag = " "
                print(found_pages.url, flag)
        else:
            print("По данному домену ничего не найдено")
        
        return results

    def history_in_table(self):
        if not self.head:
            print("Нету истории браузера")
            return

        print("\n" + "=" * 75)
        print(" URL                                               Дата посещения     ★")
        print("-" * 75)
        
        current = self.head
        
        while current:
    
            url_display = current.url[:50]
            if current.flagged:
                flag_display = "★" 
            else:
                flag_display = " "
            print(f"{url_display:<50} {current.time_clear:<20} {flag_display}")
            
            current = current.next
        
        print("=" * 75)

    def top_by_clicks(self, n=5):
        if not self.head:
            print("Нету истории браузера")
            return

        count_transit = {}
        current = self.head

        while current and current.next:
            transit_from = current.domain
            transit_to = current.next.domain
            check_transit = transit_from + " -> " + transit_to

            if check_transit in count_transit:
                count_transit[check_transit] = count_transit[check_transit] + 1
            else:
                count_transit[check_transit] = 1

            current = current.next

        top_clicks = []
        for check_transit in count_transit:
            top_clicks.append((count_transit[check_transit], check_transit))
        
        top_clicks.sort()
        top_clicks.reverse()

        print("\nТоп самых частых переходов:\n")
        
        for i in range(min(n, len(top_clicks))):
            print(str(i+1) + ". " + top_clicks[i][1] + " — " + str(top_clicks[i][0]) + " раза")
        
        print()

# Демонстрация
if __name__ == "__main__":
    history = BrowserHistory()
    
    history.add_page("https://verycooldomain.com", flagged=True)
    history.add_page("https://alsoverycooldomain.com")
    history.add_page("https://github.com")
    history.add_page("https://kinopoisk.ru")
    history.add_page("https://stackoverflow.com", flagged=True)
    history.add_page("https://youtube.com/watch?v=123")
    history.add_page("https://github.com/user/repo")
    history.add_page("https://google.com/disc")
    
    print("\n 1. Таблица истории")
    history.history_in_table()
    
    print("\n 2. Поиск по домену")
    history.domain_search("google")
    
    print("\n 3. навигация:\n")
    print("Текущая страница:", history.current.url)
    history.navigation_backward()
    print("Текущая страница:", history.current.url)
    history.navigation_backward()
    print("Текущая страница:", history.current.url)
    history.navigation_forward()
    print("Текущая страница:", history.current.url)

    print("\n 4. Топ переходов")
    history.top_by_clicks(3)

    print("\n 5. Очистка истории")
    history.clear_history()
    print("Вывод таблицы")
    history.history_in_table()