import traceback, math

class Node:
    def __init__(self, alph, freq):
        self.alph=alph
        self.freq=freq
    def __repr__(self):
        return str(self.alph)+str(':')+str(self.freq)

def huffman_encode(input_string):
    n=len(input_string)
    alph=[]
    freq=[]
    for i in input_string:
        if i in alph:          
            inde=alph.index(i)
            freq[inde]=freq[inde]+1
        if i not in alph:
            alph.append(i)
            freq.append(1)
    
    Nodelist=[]
    for i in range(len(alph)):
        a=Node(alph[i],freq[i])     
        Nodelist.append(a)
   # print(Nodelist)       
        
#--------------------------------------------------
    minQ = build_min_heap(Nodelist)
   # print(minQ)
    for i in range(len(alph)-1):
        low1=heap_extract_min(minQ)
        low2=heap_extract_min(minQ)
      #  print(low1,'low1')
     #   print(low2,'low2')
        super_alph=str(low1.alph)+str(low2.alph)
        super_freq=low1.freq+low2.freq
        super_node=Node(super_alph,super_freq)
     #   print(super_node,'super_node"')
        super_node.left=low1
        super_node.right=low2
        min_heap_insert(minQ,super_node)
        
       # print(minQ,'minQ')
    root =heap_extract_min(minQ)
   # print(root)
#-----------
    code=''
    for i in input_string:
        node=root
        while i!=node.alph:
            if i in node.left.alph:
                node=node.left
                code=code+str('0')
            elif i in node.right.alph:
                node=node.right
                code=code+str('1')
    return code
     
def build_min_heap(A):
    size=len(A) 
    for i in range(math.ceil(size/2),-1,-1):
        min_heapify(A,i) 
    return (A)

def min_heapify(A,i):
    l=2*i+1
    r=2*i+2
    if l<=len(A)-1 and A[l].freq<A[i].freq:
        m=l
    else:
        m=i
    if r<=len(A)-1 and A[r].freq<A[m].freq:
        m=r
    if m!=i:
        A[i],A[m]=A[m],A[i]
        min_heapify(A,m)
  #      print(A,'!!!!!!!!!!!!!!!!A')

def heap_extract_min(A):
    if len(A)<1:
       return None
    mini=A[0]
    A[0]=A[len(A)-1]
    A.pop()
    min_heapify(A,0)
    return mini

def min_heap_insert(A,a):
    A.append(a)
    heap_dec_key(A,len(A)-1,a)

def heap_dec_key(A,i,key):
  #  print(A,'A')
  #  print(i,'i')
  #  print(key,'key')
    if key.freq<=A[i].freq:
        while i >0 and A[(i-1)//2].freq>A[i].freq:
            A[(i-1)//2],A[i]=A[i],A[(i-1)//2]
            i=(i-1)//2
          
       

    

#  DO NOT EDIT BELOW THIS LINE

tests = ['message0.txt','message1.txt','message2.txt','message3.txt',
         'message4.txt','message5.txt']
correct = ['message0encoded.txt','message1encoded.txt',
           'message2encoded.txt','message3encoded.txt',
           'message4encoded.txt','message5encoded.txt']


#Run test cases, check whether encoding correct
count = 0

try:
    for i in range(len(tests)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading message from:",tests[i])
        fp = open(tests[i])
        message = fp.read()
        fp.close()
        print("Reading encoded message from:",correct[i])
        fp2 = open(correct[i])
        encoded = fp2.read()
        fp2.close()
        output = huffman_encode(message)
        if i < 5:
            print("Running: huffman_encode on '"+message+"'\n")
            print("Expected:",encoded,"\nGot     :",output)
        assert encoded == output, "Encoding incorrect!"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")


