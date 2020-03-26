--
-- PostgreSQL database dump
--

-- Dumped from database version 10.0
-- Dumped by pg_dump version 10.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- Data for Name: users_user; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY users_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, name, churchname, acitvesurvey, created_at, updated_at) FROM stdin;
7	argon2$argon2i$v=19$m=512,t=2,p=2$cXZONTJWSTZYVDls$k343PGHypSjVXjjYz5Aa3w	\N	f	adfasdf			adfasdf@aol.com	f	t	2017-11-28 11:51:40.170429-06			t	2018-02-07 13:02:55.986395-06	2018-02-07 13:02:56.108347-06
4	argon2$argon2i$v=19$m=512,t=2,p=2$SDVSdzV1aVNaNGFH$L6Jiealk8Uv54kS+VIWEFA	2018-01-15 16:18:38.556537-06	f	bradmaf			brhoads@maf.org	f	t	2017-11-24 16:52:29.216459-06			f	2018-02-07 13:02:55.986395-06	2018-02-07 13:02:56.108347-06
3	argon2$argon2i$v=19$m=512,t=2,p=2$YzFaNVBnZW9GSjRl$eZEKdjOrnJWqyqOU1B2gqg	2017-11-28 12:40:18.063872-06	f	brhoads			brhoads@edutechmission.org	f	t	2017-11-13 16:10:02.615053-06	Brad D Rhoads	Lakeview	f	2018-02-07 13:02:55.986395-06	2018-02-07 13:02:56.108347-06
1	argon2$argon2i$v=19$m=512,t=2,p=2$Q1o4Zjc1eEpiMWIy$uXdnUvG6EQEzV8Z2gwR0fQ	2017-11-21 16:46:21.392484-06	t	bdrhoa			bdrhoa@gmail.com	t	t	2017-11-13 15:36:08.831315-06	Brad	LVB	t	2018-02-07 13:02:55.986395-06	2018-02-07 13:02:56.108347-06
31	argon2$argon2i$v=19$m=512,t=2,p=2$SVoybFdYSFZJZzFq$8EUDlXyqxKJ4UbcGPmvcug	2018-02-06 10:39:18.356795-06	f	church2			church2@aol.com	f	t	2018-01-29 14:49:16.45987-06	church2	It still works!	t	2018-02-07 13:02:55.986395-06	2018-02-07 13:02:56.108347-06
34	argon2$argon2i$v=19$m=512,t=2,p=2$V293T2tCQ1VoRFY2$Lf2BnsKME2ST6i5W/iYlag	2018-02-09 04:11:46.251086-06	f	church4			church4@ail.com	f	t	2018-02-09 04:09:49.390883-06	Lakeview	Lakeview Bible Church	f	2018-02-09 04:09:50.337367-06	2018-02-09 04:30:44.567457-06
35	argon2$argon2i$v=19$m=512,t=2,p=2$TVQxWkVTazVsc2hz$FAzzYufwXpMCet1XBG73Ng	2018-02-09 10:27:11.296496-06	f	church6			church6@aol.com	f	t	2018-02-09 10:25:20.120083-06	Brad	Lakeview Bible Church	f	2018-02-09 10:25:20.148931-06	2018-02-09 10:32:03.17734-06
36	argon2$argon2i$v=19$m=512,t=2,p=2$dlltMlB3dGVHakxQ$JJWXDFSkNiKjm0mJiUSlyQ	2018-03-12 15:21:23.547794-06	f	church7			church7@aol.com	f	t	2018-03-12 15:20:33.890756-06			t	2018-03-12 15:20:34.093084-06	2018-03-12 15:20:34.093107-06
30	argon2$argon2i$v=19$m=512,t=2,p=2$TTAwd0NUcXJFVVVI$BHTZLC7ofsC6bX3h6ZPCtg	2018-03-13 11:37:57.913667-06	f	church1			church1@aol.com	f	t	2018-01-25 15:43:42.76551-06	Brad Rhoads	Church1	f	2018-02-07 13:02:55.986395-06	2018-03-12 15:17:13.045238-06
37	argon2$argon2i$v=19$m=512,t=2,p=2$OTA3OVdzNUxSSTJL$6JPDPCNAhEpWnxBPg9tt0g	2018-03-15 11:31:29.678595-06	f	church8			church8@aol.com	f	t	2018-03-15 11:31:00.264427-06	The Pastor	The Best Church	f	2018-03-15 11:31:00.379647-06	2018-03-15 11:33:36.666988-06
38	argon2$argon2i$v=19$m=512,t=2,p=2$QnhSQ3JNT3YxbjdT$D1pmtsaRJV2QaeUf+KrkVw	\N	f	someguy			someguy@someguy.com	f	t	2018-03-21 10:43:08.481463-06			t	2018-03-21 10:43:08.89246-06	2018-03-21 10:43:08.892482-06
\.


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY account_emailaddress (id, email, verified, "primary", user_id) FROM stdin;
5	brhoads@edutechmission.org	t	t	3
2	bdrhoa@gmail.com	t	t	1
6	brhoads@maf.org	t	t	4
7	adfasdf@aol.com	t	t	7
8	church1@aol.com	t	t	30
9	church2@aol.com	t	t	31
10	church4@ail.com	t	t	34
11	church6@aol.com	t	t	35
12	church7@aol.com	t	t	36
13	church8@aol.com	t	t	37
14	someguy@someguy.com	f	t	38
\.


--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY account_emailconfirmation (id, created, sent, key, email_address_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	auth	permission
2	auth	group
3	contenttypes	contenttype
4	sessions	session
5	sites	site
6	admin	logentry
7	account	emailconfirmation
8	account	emailaddress
9	socialaccount	socialapp
10	socialaccount	socialaccount
11	socialaccount	socialtoken
12	users	user
13	surveys	survey
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add content type	3	add_contenttype
8	Can change content type	3	change_contenttype
9	Can delete content type	3	delete_contenttype
10	Can add session	4	add_session
11	Can change session	4	change_session
12	Can delete session	4	delete_session
13	Can add site	5	add_site
14	Can change site	5	change_site
15	Can delete site	5	delete_site
16	Can add log entry	6	add_logentry
17	Can change log entry	6	change_logentry
18	Can delete log entry	6	delete_logentry
19	Can add email confirmation	7	add_emailconfirmation
20	Can change email confirmation	7	change_emailconfirmation
21	Can delete email confirmation	7	delete_emailconfirmation
22	Can add email address	8	add_emailaddress
23	Can change email address	8	change_emailaddress
24	Can delete email address	8	delete_emailaddress
25	Can add social application	9	add_socialapp
26	Can change social application	9	change_socialapp
27	Can delete social application	9	delete_socialapp
28	Can add social account	10	add_socialaccount
29	Can change social account	10	change_socialaccount
30	Can delete social account	10	delete_socialaccount
31	Can add social application token	11	add_socialtoken
32	Can change social application token	11	change_socialtoken
33	Can delete social application token	11	delete_socialtoken
34	Can add user	12	add_user
35	Can change user	12	change_user
36	Can delete user	12	delete_user
37	Can add survey	13	add_survey
38	Can change survey	13	change_survey
39	Can delete survey	13	delete_survey
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2017-11-13 15:21:50.110302-06
2	contenttypes	0002_remove_content_type_name	2017-11-13 15:21:50.121913-06
3	auth	0001_initial	2017-11-13 15:21:50.241208-06
4	auth	0002_alter_permission_name_max_length	2017-11-13 15:21:50.277076-06
5	auth	0003_alter_user_email_max_length	2017-11-13 15:21:50.291824-06
6	auth	0004_alter_user_username_opts	2017-11-13 15:21:50.307675-06
7	auth	0005_alter_user_last_login_null	2017-11-13 15:21:50.321557-06
8	auth	0006_require_contenttypes_0002	2017-11-13 15:21:50.328852-06
9	auth	0007_alter_validators_add_error_messages	2017-11-13 15:21:50.350174-06
10	auth	0008_alter_user_username_max_length	2017-11-13 15:21:50.368059-06
11	users	0001_initial	2017-11-13 15:21:50.56521-06
12	account	0001_initial	2017-11-13 15:21:50.729757-06
13	account	0002_email_max_length	2017-11-13 15:21:50.77184-06
14	admin	0001_initial	2017-11-13 15:21:50.872953-06
15	admin	0002_logentry_remove_auto_add	2017-11-13 15:21:50.910929-06
16	sessions	0001_initial	2017-11-13 15:21:50.943579-06
17	sites	0001_initial	2017-11-13 15:21:50.957281-06
18	sites	0002_alter_domain_unique	2017-11-13 15:21:50.965858-06
19	sites	0003_set_site_domain_and_name	2017-11-13 15:21:50.999322-06
20	socialaccount	0001_initial	2017-11-13 15:21:51.360503-06
21	socialaccount	0002_token_max_lengths	2017-11-13 15:21:51.466668-06
22	socialaccount	0003_extra_data_default_dict	2017-11-13 15:21:51.496203-06
23	users	0002_user_churchname	2017-11-13 18:12:35.951382-06
24	surveys	0001_initial	2017-11-17 16:28:10.422378-06
25	surveys	0002_survey_surveyid	2017-11-17 16:28:10.775632-06
26	users	0003_user_survey	2017-11-17 16:28:11.296347-06
27	surveys	0003_survey_issurveyactive	2017-11-21 14:54:06.980565-06
28	users	0004_user_acitvesurvey	2017-11-21 14:54:07.313235-06
29	surveys	0004_survey_user	2017-11-27 16:54:31.123622-06
30	users	0005_auto_20171127_2254	2017-11-27 16:54:31.717984-06
31	surveys	0005_auto_20171127_2257	2017-11-27 16:59:17.736825-06
32	surveys	0006_auto_20171128_1713	2017-11-28 11:14:07.276287-06
33	surveys	0007_auto_20171128_1731	2017-11-28 11:31:26.219349-06
34	surveys	0008_auto_20180207_1902	2018-02-07 13:02:55.887611-06
35	users	0006_auto_20180207_1902	2018-02-07 13:02:56.158684-06
36	auth	0009_alter_user_last_name_max_length	2018-03-13 11:34:06.097649-06
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
sezr4v2a0bgzml3ehtnfb01upx1b71xl	YTY2NzBkN2U3MGQyZDRjNTA4NWEzN2JkNjIxZmM5YjA2NzJjZDcwODp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YTUzYjRhZjMwMDEwNjIyMmUzYzA1NTcxYzBmNzY0NTRiYmUzZTUzIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ==	2017-12-05 15:24:49.953267-06
acjvbfs12fjio5jdv21qyt0wbt8u796i	YTY2NzBkN2U3MGQyZDRjNTA4NWEzN2JkNjIxZmM5YjA2NzJjZDcwODp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YTUzYjRhZjMwMDEwNjIyMmUzYzA1NTcxYzBmNzY0NTRiYmUzZTUzIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ==	2017-12-05 16:32:43.413055-06
udsyjq1ea9p6lbwe7s8q4dkt0ape4bxt	Mzc0M2Q0MzdkOWUwM2Y1YTlmMzIzMTgwYWIzZTFmMDU3N2M4NGFkZjp7Il9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImEzM2E2MGQ3YjkyMTRkODIzNzdiYzIyMGZhYzRiYzY4ZmUwMzZlODQifQ==	2017-12-05 16:46:21.428798-06
ee9ssgiwuok659qz14pbnlunj1euo7e8	Yjc0NmM0YjdlMjk1ZTc1Nzg3MzZhMmY2MzhiYjVlYzZmZWYxNzc1ODp7ImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGwsImFjY291bnRfdXNlciI6IjciLCJfYXV0aF91c2VyX2lkIjoiMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWE1M2I0YWYzMDAxMDYyMjJlM2MwNTU3MWMwZjc2NDU0YmJlM2U1MyIsIl9zZXNzaW9uX2V4cGlyeSI6MH0=	2017-12-12 12:40:18.408428-06
83oapzqbzoh346et0co5n6xek3l5aerb	ZGY0NDk0MDgwNTgzZmI5ZTdjZDdkN2IyYTY0NDFiYWMxYTIwMDUxYzp7ImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGwsImFjY291bnRfdXNlciI6InYiLCJfYXV0aF91c2VyX2lkIjoiMzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImU4MTA5NzNkY2U2NGRkY2NiYTM1ZGMzZTI2ZGM5NGVhNDg1ZjNkYjMiLCJfc2Vzc2lvbl9leHBpcnkiOjB9	2018-02-12 14:51:55.037694-06
fjismnur11ja9q04xgtbhuwo9455no45	OTU1YjUyYjU5NWUxY2Q0ZjZiZGYzY2RjMmM5NDU2OTYxNmRhNzRjMzp7ImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGwsImFjY291bnRfdXNlciI6IjEwIiwiX2F1dGhfdXNlcl9pZCI6IjM2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDRhODdjZjIyODA3MjNiMzliZDdiYzY2NjI5MDcxODllMDVkNGZlIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ==	2018-03-26 15:21:23.485626-06
xk5x5k2ef3lxd4jon3wpja44ut79r1ih	OTU1YjUyYjU5NWUxY2Q0ZjZiZGYzY2RjMmM5NDU2OTYxNmRhNzRjMzp7ImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGwsImFjY291bnRfdXNlciI6IjEwIiwiX2F1dGhfdXNlcl9pZCI6IjM2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDRhODdjZjIyODA3MjNiMzliZDdiYzY2NjI5MDcxODllMDVkNGZlIiwiX3Nlc3Npb25fZXhwaXJ5IjowfQ==	2018-03-26 15:21:23.773171-06
0s1tuej43vwh68tq1mt4viq95svxldym	NTk2NmNkNDA4OTZhOTllYjM5ZjhjMzcxZGRmZTM2MzEwZWEzYzQxZDp7ImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGwsImFjY291bnRfdXNlciI6IjEyIn0=	2018-04-04 10:43:13.424713-06
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY django_site (id, domain, name) FROM stdin;
1	pulse.multiplicationnetwork.org	pulsemanager
\.


--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY socialaccount_socialaccount (id, provider, uid, last_login, date_joined, extra_data, user_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY socialaccount_socialapp (id, provider, name, client_id, secret, key) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY socialaccount_socialapp_sites (id, socialapp_id, site_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY socialaccount_socialtoken (id, token, token_secret, expires_at, account_id, app_id) FROM stdin;
\.


--
-- Data for Name: surveys_survey; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY surveys_survey (surveyname, surveyid, issurveyactive, user_id, created_at, updated_at) FROM stdin;
new survey	9384	t	7	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
new survey	8685	f	3	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
new survey	4882	f	3	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
church1 - 2018-01-25T21:43:46.378309	295537	f	30	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
church1 - 2018-01-25T22:30:25.470999	129331	f	30	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
church2 - 2018-01-29T20:49:23.364830	626111	f	31	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
church2 - 2018-01-29T20:57:29.644948	546345	f	31	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
church2 - 2018-01-29T21:18:59.680277	275451	f	31	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
church2 - 2018-01-29T21:35:03.656577	683853	t	31	2018-02-07 13:02:55.098265-06	2018-02-07 13:02:55.742616-06
church4 - 2018-02-09T10:10:14.898283	353931	f	34	2018-02-09 04:10:28.456641-06	2018-02-09 04:30:44.599883-06
church6 - 2018-02-09T16:25:22.444246	535717	f	35	2018-02-09 10:25:27.512104-06	2018-02-09 10:32:03.217705-06
church1 - 2018-01-25T22:33:11.332256	256283	f	30	2018-02-07 13:02:55.098265-06	2018-03-12 15:17:13.821077-06
church7 - 2018-03-12T21:20:35.403955	245313	t	36	2018-03-12 15:20:37.489633-06	2018-03-12 15:20:37.489688-06
church8 - 2018-03-15T17:31:02.734580	873658	f	37	2018-03-15 11:31:04.265046-06	2018-03-15 11:33:36.704484-06
someguy - 2018-03-21T16:43:10.282791	832129	t	38	2018-03-21 10:43:11.910338-06	2018-03-21 10:43:11.910373-06
\.


--
-- Data for Name: users_user_groups; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY users_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: users_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: bradrhoads
--

COPY users_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('account_emailaddress_id_seq', 14, true);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('account_emailconfirmation_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('auth_permission_id_seq', 39, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('django_migrations_id_seq', 36, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('django_site_id_seq', 1, false);


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('socialaccount_socialaccount_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('socialaccount_socialapp_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('socialaccount_socialapp_sites_id_seq', 1, false);


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('socialaccount_socialtoken_id_seq', 1, false);


--
-- Name: users_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('users_user_groups_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('users_user_id_seq', 38, true);


--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bradrhoads
--

SELECT pg_catalog.setval('users_user_user_permissions_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

