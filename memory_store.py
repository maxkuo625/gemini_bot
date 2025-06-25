# 記憶暫存，可改為 Redis/DB 儲存
user_history = {}

def get_history(user_id):
    return user_history.get(user_id, [])

def append_history(user_id, role, content):
    history = user_history.get(user_id, [])
    history.append({"role": role, "parts": [content]})
    # 限制最大記憶長度
    if len(history) > 10:
        history = history[-10:]
    user_history[user_id] = history
