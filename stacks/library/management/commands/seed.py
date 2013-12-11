from django.core.management.base import NoArgsCommand
from django.template import Template, Context
from django.conf import settings
from library.models import Book


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        books = []
        book = Book()
        book.uuid = "aaa"
        book.title = "Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript, and Web Graphics"
        book.author_lastname = "Robbins"
        book.author_firstname = "Jennifer"
        book.description = """
        Do you want to build web pages, but have no previous experience? This friendly guide is the perfect place to start. You’ll begin at square one, learning how the Web and web pages work, and then steadily build from there. By the end of the book, you’ll have the skills to create a simple site with multi-column pages that adapt for mobile devices.
        
        Learn how to use the latest techniques, best practices, and current web standards—including HTML5 and CSS3. Each chapter provides exercises to help you to learn various techniques, and short quizzes to make sure you understand key concepts.
        
        This thoroughly revised edition is ideal for students and professionals of all backgrounds and skill levels, whether you’re a beginner or brushing up on existing skills.
        """
        book.isbn10 = "1449319270"
        book.publisher = "O'reilly"
        books.append(book)

        book = Book()
        book.uuid = "aab"
        book.title = "HTML and CSS: Design and Build Websites"
        book.author_lastname = "Duckett"
        book.author_firstname = "Jon"
        book.description = """
        Every day, more and more people want to learn some HTML and CSS. Joining the professional web designers and programmers are new audiences who need to know a little bit of code at work (update a content management system or e-commerce store) and those who want to make their personal blogs more attractive. Many books teaching HTML and CSS are dry and only written for those who want to become programmers, which is why this book takes an entirely new approach.

        Introduces HTML and CSS in a way that makes them accessible to everyone—hobbyists, students, and professionals—and it’s full-color throughout
        Utilizes information graphics and lifestyle photography to explain the topics in a simple way that is engaging
        Boasts a unique structure that allows you to progress through the chapters from beginning to end or just dip into topics of particular interest at your leisure
        """
        book.isbn10 = "1118008189"
        book.publisher = "Wiley"
        books.append(book)
        
        book = Book()
        book.uuid = "aac"
        book.title = "JavaScript & jQuery: The Missing Manual"
        book.author_lastname = "McFarland"
        book.author_firstname = "David"
        book.description = """
        JavaScript lets you supercharge your HTML with animation, interactivity, and visual effects—but many web designers find the language hard to learn. This jargon-free guide covers JavaScript basics and shows you how to save time and effort with the jQuery library of prewritten JavaScript code. You’ll soon be building web pages that feel and act like desktop programs, without having to do much programming.
        """
        book.isbn10 = "1449399029"
        book.publisher = "O'reilly"
        books.append(book)

        # add all the books that don't exist yet
        for book in books:
            try:
                Book.objects.get(uuid=book.uuid)
            except Book.DoesNotExist:
                book.save()
