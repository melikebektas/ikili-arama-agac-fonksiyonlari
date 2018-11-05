
from collections import namedtuple
from sys import stdout  #programın çalışması için ilgili kütüphanleri,modulleri import ettim.
 
Node = namedtuple("Node", "data, left, right")
tree = Node(1,			#düğümleri 1 den 9 a kadar olan bir ağac tanımladım.(1 kök düğüm)
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None), 
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))
 
def printwithspace(i):
    print("%i " % i)


def preorder(node, visitor = printwithspace):#preorder traverse işlemi için preorder adında bir fonksiyon oluşturdum.
	if node is not None:   #preorder traverse işlemine göre fonksiyonun gövdesini oluşturdum.
		visitor(node.data)
		preorder(node.left, visitor)
		preorder(node.right, visitor)
				
def inorder(node, visitor = printwithspace):#inorder traverse işlemi için inorder adında bir fonksiyon oluşturdum.
	if node is not None:    #inorder traverse işlemine göre fonksiyonun gövdesini oluşturdum.
		inorder(node.left, visitor)
		visitor(node.data)
		inorder(node.right, visitor)
		
def postorder(node, visitor = printwithspace):#postorder traverse işlemi için postorder adında bir fonksiyon oluşturdum.
	if node is not None:	#postorder traverse işlemine göre fonksiyonun gövdesini oluşturdum.
		postorder(node.left, visitor)
		postorder(node.right, visitor)
		visitor(node.data)
	
	
print("hoşgeldiniz lütfen yapmak istediğiniz işlemi seçin")#işlem seçimi için basit bir menu oluşturdum.
print("1.preorder")
print("2.inorder")
print("3.postorder")
print("seciminizi giriniz")
girilen=input("secim:") #kullanıcının secimi için kullanıcıdan 1 ile 3 arasında bir seçim aldım.
girilen=int(girilen)

if girilen==1:    #secim 1 ise preorder işlemini ekrana yazdırdım.
	print("\npreorder: ")
	preorder(tree)
elif girilen==2:  #secim 2 ise inorder işlemini ekrana yazdırdım.
	print("\ninorder: ")
	inorder(tree)
else:				#secim 3 ise postorder işlemini ekrana yazdırdım.
	print("\n postorder: ")
	postorder(tree)



