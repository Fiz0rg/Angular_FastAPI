My personal pet project.

I try to create internet store using Angular, FastAPI with PostgreSQL as database and Ormar as ORM.

If you have some notices, remarks, suggestions, please write me! I'll be glad to hear any rewiew!

my_contacts = {
    "telegram": https://t.me/Fiz0rg,
    "email": roma_03-96@mail.ru,
    "gmail": roma77093@gmail.com,
    "instagram": https://instagram.com/gamlet_roman?igshid=YmMyMTA2M2Y=
}


Run commands:

#command for creating redis image and will run it. Use for cache.
docker run -d --name cache --net work -p 6379:6379 redis

#command for creating relative database on postgresql with default username=postgres. 
docker run --name database -p 5432:5432 -e POSTGRES_PASSWORD=123 --net work -d postgres