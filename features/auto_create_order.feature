Feature: Auto create orders

  Scenario: Auto create orders
    Given `home` page url
     When Click Home Page class is `.floor .banner` banner randomly
     When Click product `.cat-prod-list .catpl-prod .pic` div information randomly
     Then Select class `#goods_form a.pis-color-a` color
     Then Select all `#goods_form select` visible select randomly
     Then Click class `#goods_form #_add_to_cart_out` button to add item
     Then Click class `.cart_action .btn_continue_checkout` button to continue to checkout