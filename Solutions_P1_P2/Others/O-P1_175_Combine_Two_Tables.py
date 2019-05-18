
"""
Написать SQL запрос, который воводит всех персон из таблицы Person,
не зависимо от того есть ли у них адрес

FirstName, LastName, City, State

Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.


Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

"""


"""
select FirstName, LastName, City, State
from person
left join address
on Person.PersonId = Address.PersonId

"""





