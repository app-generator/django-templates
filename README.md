# Django Templates

Cheat-sheat project for **Django Template** system to showcase the configuration and dynamic HTML page rendering. For newcomers, **Django** is a high-level Python Web framework that encourages rapid development by reusing modules and libraries built by experienced programmers. [Django Templates](https://dev.to/sm0ke/django-templates-short-introduction-and-free-samples-2878) help us to build dynamic pages, reuse components and code faster web applications. 

<br />

---

> For a **complete set of features** and long-term support, check out **[Dynamic Django](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html)**, a powerful starter that incorporates:

- ✅ [Dynamic DataTables](https://app-generator.dev/docs/developer-tools/dynamic-django/datatables.html): using a single line of configuration, the data saved in any table is automatically managed
- ✅ [Dynamic API](https://app-generator.dev/docs/developer-tools/dynamic-django/api.html): any model can become a secure API Endpoint using DRF
- ✅ [Dynamic Charts](https://app-generator.dev/docs/developer-tools/dynamic-django/charts.html): extract relevant charts without coding all major types are supported
- ✅ [CSV Loader](https://app-generator.dev/docs/developer-tools/dynamic-django/csv-loader.html): translate CSV files into Django Models and (optional) load the information
- ✅ Powerful [CLI Tools](https://app-generator.dev/docs/developer-tools/dynamic-django/cli.html) for the GIT interface, configuration editing, updating the configuration and database (create models, migrate DB)

<br />

<p align="center">
    
![Django Templates - The cover of this project.](https://user-images.githubusercontent.com/51070104/121209834-dc772980-c883-11eb-848b-03dabe31835b.png)

</p>

<br />

**How to build the project**

> **Step #1** - Clone the sources

```bash
$ git clone https://github.com/app-generator/django-templates.git
$ cd django-templates
```

<br />

> **Step #2** - Create and activate a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Install Django

```bash
$ pip install django
```

<br />

## Project Configuration

The `config` directory contains at least two relevant files:

- `config/settings.py` - global project settings
- `config/urls.py` - project routing rules

<br />

`Sample_app` directory, created with `python manage.py startapp` will serve the `html` files from `templates` directory. According to the product configuration, **HTML pages** are located in the `templates` directory.

```python
# Contents of config/settings.py
...
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # <- Specify where the directory is located

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],                     # <- Informs Django about it
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...
```

<br />

## Template Samples

> **index.html** - showcases a simple file 

On access the `ROOT` of the app or simply `index.html` a simple file is served from `templates` directory. 

<br />

> **variables.html** - Display in the HTML page a simple variable sent by the Django backend

```html
{{ variable }}
```

<br />

> **lists.html** - iterate over a simple list with integers

```html
<h4>The List:</h4>
<ul>
{% for i in list %}
<li>{{ i }}</li>
{% endfor %}
</ul>
```

<br />

> **Footer Component** - a common footer is used by all sample pages

```html
{% include "includes/footer.html" %}
```

<br />

**Thanks for reading!** Feel free to suggest more topics related to Django Templates using the `issues tracker`. 

<br />

## Resources

- [Django Templates](https://djangobook.com/mdj2-django-templates/) - a free chapter from `The Django Book` 
- [Django Templates](https://www.geeksforgeeks.org/django-templates/) - a really nice article provided by `GeeksForGeeks` platform

<br />

---
Django Templates - Open-source template project provided by AppSeed [App Generator](https://appseed.us) 
