Feature: GigaStore Point of Sale Store

  Scenario: PoS Store - Validate navigation to New customer page
    Given login to the GigaStore
    When navigate to Point of Sale store
    And click on New Customer card
    Then verify navigation to New Customer card
    And close browser
