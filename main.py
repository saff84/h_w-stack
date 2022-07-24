from Stack import Stack


if __name__ == '__main__':
    string = input('Введите строку для проверки: ')
    st = Stack()
    flag = None
    for s in string:
        if s in '({[':
            st.push(s)
        elif s in ')}]':
            if st.size() == 0:
                flag = 'Несбалансированно'
                break
            b = st.pop()
            if b == '(' and s == ')':
                continue
            if b == '{'and s == '}':
                continue
            if b == '['and s == ']':
                continue
            flag = 'Несбалансированно'
            break

    if st.isEmpty():
        flag = 'Сбалансированно'
    print(flag)




