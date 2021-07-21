def decorator(func): #hello world 를 넘겨줌
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated #함수 자체를 리턴


@decorator
def hello_world(input_text):
    print(input_text)



hello_world('Hello_world')
