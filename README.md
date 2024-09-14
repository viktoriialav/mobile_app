## Проект по автоматизации тестирования приложения My Expenses для Android
___
Содержание:
- [Исходные данные](#item-1)
- [Цель проекта](#item-2)
- [Используемые технологии](#item-3)

[//]: # (- [Тесты]&#40;#item-4&#41;)

[//]: # (- [Сборка проекта и запуск тестов]&#40;#item-5&#41;)

[//]: # (- [Отчет о прохождении тестов]&#40;#item-6&#41;)

[//]: # (- [Уведомление о прохождении тестов]&#40;#item-7&#41;)

[//]: # (- [Видео о прохождении тестов]&#40;#item-8&#41;)
___
<a id="item-1"></a>
### Исходные данные

[Cайт](https://www.myexpenses.mobi/ru/) с информацией о приложении и ссылками для скачивания с различных ресурсов.

<img align="center" src="/resources/Main_page.png" width="1000" alt="Main_page"/>

[Ссылка](https://github.com/mtotschnig/MyExpenses) на Github.
___
<a id="item-2"></a>
### Цель проекта:

Тестирование основных функций приложения, позволяющих пользователю успешно настроить приложение под себя и 
использовать основной функционал.

___
<a id="item-3"></a>
### Используемые технологии

<table width="100%" border='0'>
  <tbody>
    <tr>
      <td>Язык программирования, IDE</td>
      <td align="center">
        <a target="_blank" href="https://www.python.org/">
          <img align="center" src="/resources/Python.svg" width="40" height="40" alt="Python"/>
        </a>
        <a target="_blank" href=https://www.jetbrains.com/pycharm/>
          <img align="center" src="/resources/PyCharm.svg" width="40" height="40" alt="PyCharm"/>
        </a>
      </td>
    </tr>
    <tr>
      <td>Библиотеки, фреймворки для написания тестов</td>
      <td align="center">
        <a target="_blank" href=https://appium.io/docs/en/latest/>
          <img align="center" src="/resources/Appium1.png" width="40" height="40" alt="Appium"/>
        </a>
        <a target="_blank" href=https://github.com/yashaka/selene>
          <img align="center" src="/resources/Selene.png" width="40" height="40" alt="Selene"/>
        </a>
        <a target="_blank" href=https://docs.pytest.org/en/stable/index.html#>
          <img align="center" src="/resources/Pytest.svg" width="40" height="40" alt="Pytest"/>
        </a>
      </td>
    </tr>
    <tr>
      <td>Запуск тестов</td>
      <td align="center">
        <a target="_blank" href=https://www.jenkins.io/>
          <img align="center" src="/resources/Jenkins.svg" width="40" height="40" alt="Jenkins"/>
        </a>
        <a target="_blank" href=https://www.browserstack.com/>
          <img align="center" src="/resources/Bstack.svg" width="40" height="40" alt="Browserstack"/>
        </a>
      </td>
    </tr>
    <tr>
      <td>Формирование отчета и отправление уведомлений</td>
      <td align="center">
        <a target="_blank" href=https://qameta.io/>
          <img align="center" src="/resources/AllureTestOps.png" width="40" height="40" alt="Allure TestOps"/>
        </a>
        <a target="_blank" href=https://www.atlassian.com/ru/software/jira>
          <img align="center" src="/resources/Jira.svg" width="40" height="40" alt="Jira"/>
        </a>
        <a target="_blank" href=https://telegram.org/>
          <img align="center" src="/resources/Telegram.png" width="40" height="40" alt="Telegram"/>
        </a>
      </td>
    </tr>
  </tbody>
</table>

___
<a id="item-4"></a>
### Тесты

- Тестирование стартовых страниц и настроек:
  * Проверка заголовков всех стартовых страниц и открытия главной страницы после
  * Проверка настроек первой стартовой страницы
  * Проверка настроек второй стартовой страницы
  * Проверка настроек третьей стартовой страницы

- Тестирование основных функций главной страницы
  * Наличие основных опций на главной странице
  * Добавление расхода/дохода
  * Добавление расхода/дохода со всеми заполненными полями и проверка их содержания в детализации расхода/дохода
  * Добавление нескольких расходов/доходов
  * Удаление последнего расхода/дохода
  * Проверка работы функции "Save and create"

[//]: # (___)

[//]: # (<a id="item-5"></a>)

[//]: # (### Сборка проекта и запуск тестов)

[//]: # ()
[//]: # (Сборка, параметризация и запуск проекта производятся удаленно с помощью **Jenkins**.)

[//]: # (При каждом запросе на тестирование браузера **Selenoid** запускает новый **Docker**-контейнер и )

[//]: # (останавливает его после закрытия браузера. Параметр, который можно изменить перед запуском проекта, - это версия браузера **Chrome**.)

[//]: # ()
[//]: # (Для запуска проекта необходимо:)

[//]: # (- Перейти по [ссылке]&#40;https://jenkins.autotests.cloud/job/14_vic_lav_selectel/&#41; к проекту в **Jenkins**)

[//]: # (- Нажать **"Build with Parameters"**)

[//]: # (- Выбрать версию браузера &#40;или оставить значение по умолчанию&#41;)

[//]: # (- Нажать **"Build"**)

[//]: # ()
[//]: # (<p>)

[//]: # (<img src="resources/Jenkins_Build_with_Parameters.png" width="1000" alt="Press Build with Parameters">)

[//]: # (</p>)

[//]: # (<p>)

[//]: # (<img src="resources/Jenkins_Browser_version_Build.png" width="1000" alt="Press Build">)

[//]: # (</p>)

[//]: # ()
[//]: # ()
[//]: # (Все необходимые настройки проекта и команды запуска можно посмотреть во вкладке **"Configure"** проекта в **Jenkins**.)

[//]: # ()
[//]: # (___)

[//]: # (<a id="item-6"></a>)

[//]: # (### Отчет о прохождении тестов)

[//]: # ()
[//]: # (Отчет формируется в **Allure Report** автоматически после прохождения тестов.   )

[//]: # (Если проект запущен удаленно, его можно открыть прямо из **Jenkins** для интересующего запуска проекта, кликнув на)

[//]: # (иконку **Allure Report**.  )

[//]: # (В случае локального запуска проекта, в терминале необходимо выполнить команду:)

[//]: # ()
[//]: # (```shell)

[//]: # (allure serve allure-results)

[//]: # (```)

[//]: # ()
[//]: # (<p>)

[//]: # (<img src="resources/Allure_report.png" width="1000" alt="Allure Report">)

[//]: # (</p>)

[//]: # ()
[//]: # (___)

[//]: # (<a id="item-7"></a>)

[//]: # (### Уведомление о прохождении тестов)

[//]: # ()
[//]: # (Проект в **Jenkins** настроен таким образом, чтобы уведомления приходили в конкретный чат )

[//]: # (приложения **Telegram**.)

[//]: # ()
[//]: # (<p>)

[//]: # (<img src="resources/Telegram_message.png" width="350" alt="Message from Telegram">)

[//]: # (</p>)

[//]: # ()
[//]: # (___)

[//]: # (<a id="item-8"></a>)

[//]: # (### Видео о прохождении тестов)

[//]: # (Ниже приведены видео о прохождении тестов, запущенных)

[//]: # (- удаленно на Browserstack)

[//]: # (<p>)

[//]: # (<img src="resources/video_tests.gif" alt="Selenoid Video">)

[//]: # (</p>)

[//]: # (- локально на Browserstack)

[//]: # (<p>)

[//]: # (<img src="resources/video_tests.gif" alt="Selenoid Video">)

[//]: # (</p>)

[//]: # (- локально для эмулятора)

[//]: # (<p>)

[//]: # (<img src="resources/video_tests.gif" alt="Selenoid Video">)

[//]: # (</p>)

[//]: # (- локально на реальном устройстве)

[//]: # (<p>)

[//]: # (<img src="resources/video_tests.gif" alt="Selenoid Video">)

[//]: # (</p>)