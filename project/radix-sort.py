import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    byteBook = book_to_words()
    firstWordByte = byteBook[0]
    print(len(firstWordByte))
    firstWordByte += bytes(10 - len(firstWordByte))
    print(firstWordByte)
    print(byteBook)
    longest = byteBook[0]
    for x in byteBook:
      if len(x) > len(longest):
        longest = x

    for x in range(len(byteBook)):
      byteBook[x] += bytes(len(longest) - len(byteBook[x]))

    def radix_sort (arr, index):
      count = [0]*128
      newa = ['']*128

      for i in range(len(arr)):
        count[arr[i][-1 * index]] += 1
      
      psum = 0
      for i in range(len(count)):
        psum += count[i]
        count[i] = psum
      
      for i in range(len(arr) - 1, -1, -1):
        count[arr[i][-1 * index]] -= 1
        newa[arr[i][-1 * index]] = arr[i]

      for i in range(len(count)):
        count[i] = 0

      if index < 31:
        radix_sort(arr, index + 1)
      else:
        end = 0
        for x in range(len(newa)):
          for y in range(len(newa[x])-1):
            if str(newa[x])[y] == '\\' and str(newa[x])[y+1] == 'x':
              end = y
              break
          newa[x] = str(newa[x])[2:end]
        sub = 0
        for i in range(len(newa)):
          if newa[i-sub] == '':
            del newa[i-sub]
            sub += 1
        print(newa)
        return newa
    
    radix_sort(byteBook, 28)

radix_a_book()
