
# BEEN DECIDED IT IS UNEEDED
# It causes a global singleton that fastAPI doesn't reall need

# from threading import Lock

# # Used as a decorator to make a class have a single instance
# # This also uses Lock to prevent things to overtake eachother in
# # race conditions with threading
# # You are going to use this decorator on classes
# # That will be part of fastAPI Depends which will do the lock
# # threading protection on its own
# # BUT for knowledge and overkill its here!
# def singleton(cls):
#     instances = {}
#     lock = Lock()  # Thread-safe lock

#     def get_instance(*args, **kwargs):
#         if cls not in instances:
#             with lock:  # Ensure only one thread can create the instance
#                 if cls not in instances:  # Double-check to avoid race conditions
#                     instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return get_instance
