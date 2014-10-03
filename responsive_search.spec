
=========================================================================================
# Header
logo                          id     svg-logo
header-left                   id     header-column-left
header-right                  id     header-column-right
hamburger                     css    .side-menu-button .icon

# Search bar
place-ad-button               id     search-syi-button
search-categories             id     search-categories
search-distances              id     search-distances
search-button                 id     search-button
lens-icon                     css    .icon-mp-search
search-advanced               css    #search-content fieldset.advanced

# Sidebar
sidebar                       id     left-column-container

# Search results
navigation                    css    .results-nav-top
search-result-odd             css    .search-results-table .row.group-1
search-result-even            css    .search-results-table .row.group-0
pagination-bottom             id      pagination
pagination-button-previous    css    .pagination .pagination-previous
pagination-button-next        css    .pagination .pagination-next
previous-icon                 css    .pagination .button .icon
next-icon                     css    .pagination .button .icon # cannot distinguish previous and next icon's locators

# Footer
footer-navigation             id     footer-navigation
footer-links                  css    .footer-links
disclaimer                    id     footer-disclaimer
ebay-logo                     id     footer-ebay

=========================================================================================


@all
-----------------------------------------------------------------------------------------
logo, search-button, header-right, footer-navigation, footer-links, disclaimer, ebay-logo, pagination-button-previous, pagination-button-next
    visible

footer-links
    text contains: Aanbieding
    text contains: Voorwaarden en Privacybeleid

pagination-button-previous
    contains: previous-icon

pagination-button-next
    contains: next-icon


@mobile
-----------------------------------------------------------------------------------------
hamburger
    visible

header-left, place-ad-button, search-categories, search-distances, navigation, sidebar
    absent

header-right
    contains: hamburger

search-button
    contains: lens-icon

# this fails sometimes if banner pops up
search-result-odd, search-result-even
    color scheme: >50% #ffffff

pagination-bottom
    text contains: Pagina 1 van

pagination-button-previous, pagination-button-next
    text is: 

footer-navigation
    text is: Andere groepen

ebay-logo:
    below: disclaimer 5 to 15 px


@tablet
-----------------------------------------------------------------------------------------
hamburger, header-left, place-ad-button, navigation, sidebar
    absent

header-right
    text ends: Mijn Marktplaats

search-categories
    visible
    width: 300 to 310px
    above: search-distances 1 to 10px

search-button
    text is: Zoek

# this fails sometimes if banner pops up
search-result-odd, search-result-even
    color scheme: >50% #ffffff

pagination-bottom
    text contains: 1 2 3 4 5

pagination-button-previous
    text is: Vorige

pagination-button-next
    text is: Volgende

footer-navigation
    text contains: Caravans en Kamperen

footer-links
    text contains: Help en Info

ebay-logo:
    below: disclaimer 5 to 15px


@desktop
-----------------------------------------------------------------------------------------
hamburger
    absent

header-left, place-ad-button, navigation, sidebar
    visible

header-right
    text ends: Veilig handelen

search-categories
    visible
    width: 150 to 160px
    near: search-distances 50 to 100px left

search-button
    text is: Zoek

# this fails sometimes if banner pops up
search-result-odd
    color scheme: >50% #fffbe7

# this fails sometimes if banner pops up
search-result-even
    color scheme: >50% #fef5c6

pagination-bottom
    text contains: 1 2 3 4 5

pagination-button-previous
    text is: Vorige

pagination-button-next
    text is: Volgende

footer-navigation
    text contains: Caravans en Kamperen

footer-links
    text contains: Help en Info Voorwaarden en Privacybeleid

ebay-logo:
    near: disclaimer 90 to 110px right