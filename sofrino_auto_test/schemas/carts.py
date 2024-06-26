mini_cart_view = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "allAmounts": {
            "type": "integer"
        },
        "cartItemsDetailed": {
            "type": "array",
            "items": {}
        },
        "medias": {
            "type": "array",
            "items": {}
        },
        "allSumm": {
            "type": "integer"
        },
        "allOldSumm": {
            "type": "integer"
        },
        "allAmountsBadge": {
            "type": "string"
        },
        "moreText": {
            "type": "string"
        },
        "hasStop": {
            "type": "boolean"
        }
    },
    "required": [
        "allAmounts",
        "cartItemsDetailed",
        "medias",
        "allSumm",
        "allOldSumm",
        "allAmountsBadge",
        "moreText",
        "hasStop"
    ]
}

add_item = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "product_id": {
            "type": "integer"
        },
        "props": {
            "type": "array",
            "items": {}
        },
        "amount": {
            "type": "string"
        }
    },
    "required": [
        "product_id",
        "props",
        "amount"
    ]
}

add_item_2 = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "amount": {
            "type": "integer"
        }
    },
    "required": [
        "amount"
    ]
}

del_item = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "allAmounts": {
            "type": "integer"
        },
        "cartItemsDetailed": {
            "type": "array",
            "items": {}
        },
        "medias": {
            "type": "array",
            "items": {}
        },
        "allSumm": {
            "type": "integer"
        },
        "allOldSumm": {
            "type": "integer"
        },
        "allAmountsBadge": {
            "type": "string"
        },
        "moreText": {
            "type": "string"
        },
        "hasStop": {
            "type": "boolean"
        }
    },
    "required": [
        "allAmounts",
        "cartItemsDetailed",
        "medias",
        "allSumm",
        "allOldSumm",
        "allAmountsBadge",
        "moreText",
        "hasStop"
    ]
}

view_all_product_in_cart = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "liked": {
      "type": "array",
      "items": {}
    },
    "compared": {
      "type": "array",
      "items": {}
    },
    "carted": {
      "type": "object",
      "properties": {
        "allCartAmount": {
          "type": "integer"
        },
        "cartItemsAmounts": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "allCartAmount",
        "cartItemsAmounts"
      ]
    }
  },
  "required": [
    "liked",
    "compared",
    "carted"
  ]
}