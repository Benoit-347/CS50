def get_prefix(number = 999):
    units = ["","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen",
            "sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    output = ""
    if number // 100:
        output =  units[number//100] + ' hundred'
        number = number - (number //100)*100
    if number %100:
        if number >=20:
            output = ' '.join([output, tens[number //10]]).strip()
            if number %10 and number //1:
                output = output + '-' + units[number%10]
                return output
        elif number >9:
            output = ' '.join([output, teens[number-10]]).strip()
            return output
    if number %10 and number //1:
        output = ' '.join([output, units[number%10]]).strip()

    return output

print(get_prefix(999))
print(get_prefix(625))
print(get_prefix(605))
print(get_prefix(100))
print(get_prefix(45))
print(get_prefix(20))
print(get_prefix(19))
print(get_prefix(11))
print(get_prefix(10))
print(get_prefix(9))
print(get_prefix(1))
print(get_prefix(0))