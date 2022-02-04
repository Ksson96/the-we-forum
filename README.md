## Data Storage

### Post Table
| Database Key  	| Type           	| Relationship 	|
|---------------	|----------------	|--------------	|
| post_id       	| Int(Unique)    	| PrimaryKey   	|
| title         	| Char(300)      	|              	|
| author        	| User model     	| ForeignKey   	|
| content       	| TextField      	|              	|
| created_date  	| DateTime       	|              	|
| updated_date  	| DateTime       	|              	|
| category_name 	| Category model 	| ForeignKey   	|
| likes         	| User model     	| ManyToMany   	|
