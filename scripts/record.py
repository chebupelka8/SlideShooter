def write_score(score, filename):
    file = open(filename, 'w')
    file.write(str(score))
    file.close()
    
def get_max_score(filename):
    file = open(filename, 'r')
    score = int(file.read())
    file.close()
    return score

