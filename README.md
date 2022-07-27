# Biographify [website](https://biographify.herokuapp.com)

![Project Image](https://raw.githubusercontent.com/EdwardX29/biographify/main/.github/images/projectImage.png)

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [Author Info](#author-info)

---

## Description

Inpsired by [receiptify](https://receiptify.herokuapp.com/), this website generates a biography-esque aesthetic for a Spotify user's top tracks for 1 month, 6 months, and all time. 

After signing in with Spotify SSO, this project makes requests to Spotify API to retrieve a user's top tracks. Tracks are then formatted into a biography aesthetic and can be downloaded as png files.

#### Technologies

- Python Django MVT
- Bootstrap 4
- Spotify API

[Back To The Top](#biographify-website)

---

## How To Use

#### Installation
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

[Back To The Top](#biographify-website)

---

## References
[Back To The Top](#biographify-website)

---

## Author Info

- Github - [EdwardX29](https://github.com/EdwardX29)

[Back To The Top](#biographify-website)
