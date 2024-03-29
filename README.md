#django-brdesigner
=================
##Description
Reusable components that help make building a customizable and extendable Django project easier.


##Concepts
###Pages
- **models.Page**: Used to store basic properties about an HTML page (e.g. title, path, meta tags)
- **models.MenuItem**: Represents an item in a menu that links to either a Page or an external link
- **models.PageType**: Used to map a Page to a view controller

###Styles
- **models.CssSelector**: Css selector including a list of CssSetting
- **models.CssSetting**: Css setting
- **models.CssFileLoad**: Css files to load in HTML head

###Templates
- **templates/brdesigner/base.djhtml**: Template with some basic HTML structure leveraging other brdesigner concepts

###App Js
- **static/brdesigner/js/core_br.js**: Instantiates common app js vars
- **models.JsFileLoad**: Javascript files to load in HTML head

###Branding
- **models.Brand**: Branding info (e.g. logos, favico)

###Admin
- **admin.BadRacketAdminBase**: Sets up common admin features (e.g. sortable js and textareas)
- **models.SortableModel**: Abstract base class that provides sorting concepts supported by the admin


##Installation

##Author
