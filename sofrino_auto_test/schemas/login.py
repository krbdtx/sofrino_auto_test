login_error = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "loginErrors": {
      "type": "string"
    }
  },
  "required": [
    "loginErrors"
  ]
}

login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "action": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "password": {
      "type": "string"
    }
  },
  "required": [
    "action",
    "email",
    "password"
  ]
}

login_success = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "loginSuccess": {
      "type": "boolean"
    }
  },
  "required": [
    "loginSuccess"
  ]
}

