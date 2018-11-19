from random import randint, shuffle

def get_valid_payload():
    payload = {}
    payload["id"] = {}
    payload["type"] = ""
    payload["source"] = ""
    payload["title"] = ""
    payload["action"] = "create"
    payload["version"] = 1
    payload["timestamp"] = "2004-02-12T15:19:21+03:00"

    return payload

def get_invalid_payload():
    payload = get_valid_payload()
    invalid_values = [
        ("id", "id"),
        ("version", "1"),
        ("action", "unknown"),
        ("source", None),
        ("timestamp", "2004-13-12T15:19:21+03:00")
    ]
    for _ in range(0, randint(1, len(invalid_values))):
        shuffle(invalid_values)
        value = invalid_values.pop(
            randint(0, len(invalid_values)-1)
        )
        if value[1] is not None:
            payload[value[0]] = value[1]
        else:
            payload.pop(value[0], None)
    return payload