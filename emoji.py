emoji={'happy':'😁','sad':'😢','angry':'😡','pizza':'🍕'}
n=input("message:")
if 'happy' in n:
    n=n.replace('happy',emoji['happy'])
    print(n)
elif 'sad' in n:
    n=n.replace('sad',emoji['sad'])
    print(n)
elif 'angry' in n:
    n=n.replace('angry',emoji['angry'])
    print(n)
else:    
    n=n.replace('pizza',emoji['pizza'])
    print(n)
    exit