# Patika Insertion Sort Project

## Proje1

[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

Big-O gösterimini yazınız.

Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız.

  1. Average case: Aradığımız sayının ortada olması
  2. Worst case: Aradığımız sayının sonda olması
  3. Best case: Aradığımız sayının dizinin en başında olması.

[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

## Çözüm

### Insertion Sort
* [***22***,***27***,16,2,18,6]
* [22,***27***,***16***,2,18,6] >> [22,***16***,***27***,2,18,6]
* [***22***,***16***,27,2,18,6] >> [***16***,***22***,27,2,18,6]
* [16,22,***27***,***2***,18,6] >> [16,22,***2***,***27***,18,6]
* [16,***22***,***2***,27,18,6] >> [16,***2***,***22***,27,18,6]
* [***16***,***2***,22,27,18,6] >> [***2***,***16***,22,27,18,6]
* [2,16,22,***27***,***18***,6] >> [2,16,22,***18***,***27***,6]
* [2,16,***22***,***18***,27,6] >> [2,16,***18***,***22***,27,6]
* [2,***16***,***18***,22,27,6]
* [2,16,18,22,***27***,***6***] >> [2,16,18,22,***6***,***27***]
* [2,16,18,***22***,***6***,27] >> [2,16,18,***6***,***22***,27]
* [2,16,***18***,***6***,22,27] >> [2,16,***6***,***18***,22,27]
* [2,***16***,***6***,18,22,27] >> [2,***6***,***16***,18,22,27]
* [***2***,***6***,16,18,22,27]

### Big O Notation
O(n^2)

### Case
[2,6,16,***18***,22,27] dizinin orta kısmında bulunduğundan dolayı ***Average Case*** kapsamına girer.

### Selection Sort
* [7,3,5,8,2,9,4,15,6] >> [***2***,3,5,8,7,9,4,15,6]
* [2,3,5,8,7,9,4,15,6] >> [2,***3***,5,8,7,9,4,15,6]
* [2,3,4,8,9,7,5,15,6] >> [2,3,***4***,8,9,7,5,15,6]
* [2,3,4,5,9,7,8,15,6] >> [2,3,4,***5***,9,7,8,15,6]
* [2,3,4,5,6,7,8,15,9] >> [2,3,4,5,***6***,7,8,15,9]
* [2,3,4,5,6,7,8,15,9] >> [2,3,4,5,6,***7***,8,15,9]
* [2,3,4,5,6,7,8,15,9] >> [2,3,4,5,6,7,***8***,15,9]
* [2,3,4,5,6,7,8,9,15] >> [2,3,4,5,6,7,8,***9***,15]
