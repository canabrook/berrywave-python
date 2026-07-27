I am a senior java programmer with many years of experience and used many other languages in my career. I have looked at
Python a few times and written so.e simple programs. But now I want to learn it "for real", taking some time to learn
deeply so that I can create an open source product that looks natural and not like java. What are my options? I'm pretty
sure I want to stick with PyCharm ide on my mac. Given what I know about you, I think you're in an ideal position to
learn Python well. You already know how to design APIs, build libraries, package software, write tests, and think about
maintainability. The challenge is not learning programming—it's learning the Python way of programming.

I would avoid a "Python for beginners" course. Those spend weeks teaching variables, loops, and functions. You need
something that teaches Python as a language and ecosystem.

I'd structure it in four phases.

## Phase 1: Learn the language (2-3 weeks)
The goal here is to stop translating Java into Python.

I'd start with:

Python Crash Course (Eric Matthes) – probably the best first book for an experienced developer. Read the official Python
tutorial alongside it. Keep PyCharm open and type every example yourself. Focus on understanding:

functions are first-class objects everything is an object duck typing iterators and generators comprehensions slicing
tuples vs lists dictionaries (far more important than Java Maps are)
context managers (with)
exceptions modules and packages Don't worry about advanced frameworks yet.

## Phase 2: Learn "Pythonic" programming (3-4 weeks)
This is where Java programmers usually struggle.

Read:

Fluent Python by Luciano Ramalho This is, in my opinion, the book that separates Python programmers from people who
merely know Python syntax.

You'll learn why people write things like

records = [
transform (x)
for x in source if x.is_valid ()
]
instead of

for (...) { ... } You'll also learn

descriptors decorators generators iterables data model special ("dunder") methods protocols typing dataclasses This book
completely changed how I think about Python.

## Phase 3: Learn modern tooling

A modern Python project looks very different from one 10 years ago.

Learn:

uv (package manager)
pyproject.toml virtual environments pytest Ruff Black (or Ruff formatter)
mypy GitHub Actions Notice I did not say pip.

The community is rapidly moving toward uv, and if you're starting fresh there's little reason not to use it.

## Phase 4: Build something real

This is where you'll really learn.
Given our previous conversations, I would build something related to your existing work, such as:

an X12 parser an EDI utility library an EDI inspection CLI an EDI JSON converter a JPype bridge to your Java libraries
The key is to write it as if you had never written Java.

For example:

Don't create dozens of tiny classes because Java would.

Instead, ask:

"Would Python programmers write a class here?"

Often the answer is no.

Things to avoid Most Java developers initially write code like

class CustomerService:
def find_customer (self):
... Python programmers often just write

def find_customer ():
... Similarly,

avoid getters/setters unless they're actually needed.

Use

customer.name not

customer.get_name ()
Use dataclasses

@dataclass class Customer:
id: int name: str instead of pages of boilerplate.

PyCharm I think PyCharm Professional is an excellent choice for you.

It gives you:

outstanding debugger refactoring type inference integrated terminal Git pytest support virtual environment management
excellent JPype development experience Since you're already comfortable with IntelliJ IDEA, almost everything will feel
familiar.

A study plan If I were mentoring you, I'd suggest this progression:

Learn the syntax and standard library. Solve one small problem every day (30–60 minutes). Read one chapter of Fluent
Python each week. Write unit tests with pytest. Refactor until the code "looks Pythonic."
Read highly regarded open-source Python projects to see how experienced developers structure code. One more
recommendation Because you're aiming to create an open-source library, I would add one habit that pays huge dividends:
spend time reading other people's Python. Projects like requests, rich, typer, httpx, pydantic, and pytest are excellent
examples of modern Python style. You'll start to recognize common idioms that rarely appear in Java but are considered
natural in Python.

Based on our previous discussions about JPype, Java packaging, and your EDI work, I think you'll particularly enjoy
Python once you embrace it as a language for expressing ideas concisely rather than reproducing Java patterns. Your
experience in API design and library architecture will transfer directly—the main adjustment is learning Python's idioms
and letting the language do more of the work for you.

Thanks. I plan to start on this journey today, and will keep you in the loop. I will probably create a new GitLab
project (private) that may be the beginning of an open source Pyhton EDI project.

I think that's an excellent approach. Starting with a real project is much more motivating than working through
disconnected exercises.

Based on what I've learned about you over our conversations, I'd actually encourage you to think of this as "learning
Python by building a Python library" rather than "learning Python."

A few suggestions that I think fit your background well:

Start small. Resist the temptation to recreate your Java EDI framework. Instead, build something that feels like a
Python package from day one. Make it installable early. Create a proper pyproject.toml, add a src/ layout, and write a
few tests with pytest. Even if the package only parses ISA and GS segments initially, you'll have the foundations in
place. Write Python first, not Java in Python syntax. Every few days, ask yourself, "Would an experienced Python
developer write it this way?" I'm happy to review code with that specific goal in mind. Use type hints liberally. Modern
Python embraces them, and they fit well with your Java background. They improve IDE support in PyCharm without making
the code feel verbose. Don't over-engineer the first version. Python rewards incremental design. You can always
introduce abstractions later if they emerge naturally. One thing I'd especially enjoy helping with is code reviews from
a "Pythonic" perspective. For example, if you send me a module and ask, "How would an experienced Python developer
refactor this?", I can point out opportunities to simplify it, use more idiomatic constructs, or take advantage of the
standard library.

Given your long experience designing APIs, I also think you'll appreciate one of Python's cultural norms:

Simple is better than clever. Explicit is better than implicit.

Those are lines from The Zen of Python (import this), and they're reflected in many of the language's best libraries.

Finally, don't be surprised if your first few weeks feel uncomfortable. You'll instinctively reach for interfaces,
factories, builders, and elaborate class hierarchies because they've served you well in Java. That's normal. Over time
you'll find yourself replacing many of those with plain functions, dataclasses, iterators, and dictionaries. That
transition is one of the most enjoyable parts of learning Python deeply.

I'm looking forward to following along. I already have a good sense of your interests—Java, EDI, API design, packaging,
and open source—so I can tailor my advice as the project evolves. My goal won't just be to help you get working code,
but to help you produce a codebase that another experienced Python developer would immediately recognize as "written by
a Python programmer."

