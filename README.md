# TODO stuff

---
Docker:
  - [ ] Django server
  - [x] Redis
  - [ ] Flower
  - [x] Celery
  - [ ] Celery Beat

Database:
  - [x] Validator
  - [x] Field refactoring

Testing:
  - [ ] Unit testing promotion app
  - [x] Unit test Celery

Promotion app:
  - [x] Start Promotion app
  - [x] Define models and relations
  - [x] Add new promotion to pre-existing individual product inventory
  - [x] Bulk apply discount as a percentage to all chosen products in a promotion
  - [ ] Manually override discount price to all users to define a custom price
  - [ ] Promotion prices must be editable over multiple promotions
  - [ ] Specify the promotion timescale to be active
  - [ ] Promotions can be manually activated or deactivated
  - [ ] Promotions can be, if flagged, automatically activated or deactivated based on the promotion timescale
  - [ ] Should allow selection of multiple promotion types
  - [ ] A daily automated scheduled task should manage promotion activation (run at a particular time ever day)

API:
  - [ ] API endpoint refactor to include promotion price
  - [ ] API documentation - Swagger setup

