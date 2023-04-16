# Rashifal API in Flask

This is a very simple API that get the data about rashifal for the day, for the week, for the month and for the year. The data for the week cannot be accessed right now but I will soon add that feature

## Base URL

```python
"https://python.ankurgajurel.com.np/rashifal"
```

## Authentication

At the moment, I have not implemented authentication to this API.

## Endpoints

### 'GET /'

Retrieves the Home Page

<p>Parameters</p>

No parameters.

Example request:

```python
import requests
base_url = "https://python.ankurgajurel.com.np/rashifal"
response = requests.get(base_url).text
print(response)
```

### 'GET /daily[rashi]'

<p>Parameters</p>

- "rashi": The rashi you want to get the data for

Example request:

```python
import requests
base_url = "https://python.ankurgajurel.com.np/rashifal"
work_url = base_url + "/daily"
rashi = "singha"
response = requests.get(work_url + "/" + rashi).text
print(response)
```

### 'GET /monthly/[rashi]'

<p>Parameters</p>

- "rashi": The rashi you want to get the data for

Example request:

```python
import requests
base_url = "https://python.ankurgajurel.com.np/rashifal"
work_url = base_url + "/monthly"
rashi = "singha"
response = requests.get(work_url + "/" + rashi).text
print(response)
```

### 'GET /yearly/[rashi]'

<p>Parameters</p>

- "rashi": The rashi you want to get the data for

Example request:

```python
import requests
base_url = "https://python.ankurgajurel.com.np/rashifal"
work_url = base_url + "/yearly"
rashi = "singha"
response = requests.get(work_url + "/" + rashi).text
print(response)
```