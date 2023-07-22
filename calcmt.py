import queue
import threading

def user_input():
    while True:
        expression = input("Math expression goes here (or 'exit' to quit): ")
        if expression.lower() == "exit":
            break
        result_queue.put(expression)

def calculate():
    while True:
        expression = result_queue.get()
        if expression is None:
            break
        try:
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            result_queue.task_done()

if __name__ == "__main__":
    result_queue = queue.Queue()

    input_thread = threading.Thread(target = user_input)
    calc_thread = threading.Thread(target = calculate)

    input_thread.start()
    calc_thread.start()

    input_thread.join()
    result_queue.put(None)  #  thread to exit
    calc_thread.join()

#                               Taombawkry                  '''   9  '''
