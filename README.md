# < CHWM := CHAVIERWEBMÍDIA >

## 🌐 Site ChavierWebMídia

Projeto de desenvolvimento do site profissional **ChavierWebMídia**, criado para apresentar serviços, projetos e trabalhos desenvolvidos na área de desenvolvimento web.

## 🎯 Objetivo

Criar um site profissional, responsivo e organizado para divulgação dos trabalhos da **ChavierWebMídia**.

## 🛠️ Tecnologias

* Python
* Django
* HTML5
* CSS3
* Bootstrap 5.3.3
* Bootstrap Icons
* Git
* GitHub

## 📁 Estrutura inicial

```text
site_chavierwebmidia_2026/
│
├── chavierwebmidia/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── includes/
│   │       ├── header.html
│   │       └── footer.html
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── manage.py
├── requirements.txt
└── README.md
```

## 🎨 Layout

O projeto utiliza **Bootstrap** para construção do layout responsivo.

Padrão utilizado no Grid:

```html
col-12 col-md-6 col-lg-4
```

### Responsividade

* `col-12`: dispositivos pequenos
* `col-md-6`: dispositivos médios
* `col-lg-4`: dispositivos grandes

## 🧩 Componentes

### Base

Foi criado um `base.html` para servir como estrutura principal das páginas.

Utilização de:

```django
{% extends 'base.html' %}
```

### Header

Header responsivo utilizando Bootstrap com menu de navegação.

### Footer

Footer responsivo utilizando o **Grid System do Bootstrap**.

Estrutura:

```text
container
└── row
    ├── col-12 col-md-6 col-lg-4
    ├── col-12 col-md-6 col-lg-4
    └── col-12 col-md-6 col-lg-4
```

### Home

A página inicial possui:

* Apresentação
* Serviços
* Projetos
* Contato

## 🎨 Cores

As principais cores do projeto foram organizadas utilizando variáveis CSS no `:root`.

```css
:root {
    --cor-principal: #000e24;
    --cor-secundaria: #090979;
    --cor-destaque: #00d4ff;
    --cor-fundo: #333333;
    --cor-branca: #ffffff;
    --cor-texto: #333333;
}
```

Também foi utilizado um gradiente no Header e Footer.

## 📱 Responsividade

O projeto utiliza as classes responsivas do Bootstrap para adaptar o conteúdo a:

* 📱 Celulares
* 📱 Tablets
* 💻 Desktops

## 🚧 Status do projeto

**Em desenvolvimento.**

Novas páginas, conteúdos, funcionalidades e melhorias de layout serão adicionados durante o desenvolvimento do projeto.

## 👨‍💻 Desenvolvedor

**ChavierWebMídia**

Desenvolvimento de:

* Sites Profissionais
* Landing Pages
* Sistemas Web
