# !/usr/bin/env python

def checkBox(box):
    chars = {}
    two = False
    three = False
    for c in box:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for k in chars:
        if chars[k] is 2:
            two = True
        if chars[k] is 3:
            three = True
    return (two, three)
        
def getDiffs(box1, box2):
    diffs = []
    for i in range(0,len(box1)):
        if box1[i] is not box2[i]:
            diffs.append(i)
    return diffs

if __name__ == '__main__':
    f = open('assets/02.txt', 'r')
    boxes = [x.rstrip() for x in f]
    
    # Part 1
    twos = 0
    threes = 0
    for box in boxes:
        checked = checkBox(box)
        if checked[0]:
            twos += 1
        if checked[1]:
            threes += 1
        
    print(f'checksum: {twos*threes}')

    # Part 2
    for i in range(0, len(boxes)):
        for j in range(i+1, len(boxes)):
            diffs = getDiffs(boxes[i], boxes[j])
            if len(diffs) is 1:
                print(boxes[i])
                print(boxes[j])
                print(boxes[i][:diffs[0]]+boxes[i][diffs[0]+1:])
                break

        


