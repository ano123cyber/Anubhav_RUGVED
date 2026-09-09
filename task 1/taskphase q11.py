<<<<<<< HEAD
def grade_level():
    text=input("Enter your text:")
    letter_count=0
    word_count=0
    sentence_count=0
    sine=text.split()
    word_count=len(sine)
    if word_count==0:
        print("Grade:Below Kindergarten")
        return
    for i in text:
        if i.isalnum():
            letter_count+=1
        if i=='.' or i=='!' or i=='?':
            sentence_count+=1
    if sentence_count==0:
        sentence_count=1
    avg_letters=(letter_count/word_count)*100 #Average letters per 100 words
    avg_sentences=(sentence_count/word_count)*100 #Average sentences per 100 words
    value=(0.0588*avg_letters)-(0.296*avg_sentences)-15.8 # Coleman-Lieu formula
    grade1=int(value+0.5)
    if grade1>=16:
        print("Grade level is 16+(College graduate")
    elif grade1<1:
        print("Grade level is below kindergarten")
    else:
        print("The grade level is:",grade1)
grade_level()


=======
def grade_level():
    text=input("Enter your text:")
    letter_count=0
    word_count=0
    sentence_count=0
    sine=text.split()
    word_count=len(sine)
    if word_count==0:
        print("Grade:Below Kindergarten")
        return
    for i in text:
        if i.isalnum():
            letter_count+=1
        if i=='.' or i=='!' or i=='?':
            sentence_count+=1
    if sentence_count==0:
        sentence_count=1
    avg_letters=(letter_count/word_count)*100 #Average letters per 100 words
    avg_sentences=(sentence_count/word_count)*100 #Average sentences per 100 words
    value=(0.0588*avg_letters)-(0.296*avg_sentences)-15.8 # Coleman-Lieu formula
    grade1=int(value+0.5)
    if grade1>=16:
        print("Grade level is 16+(College graduate")
    elif grade1<1:
        print("Grade level is below kindergarten")
    else:
        print("The grade level is:",grade1)
grade_level()


>>>>>>> 0cdc8ead437185b27036fa68df9277ec1534e39a
