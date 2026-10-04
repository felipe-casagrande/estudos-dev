--
-- PostgreSQL database dump
--

\restrict zYTY0NrCR41eKxIiCvsjPW2Ii5hBkL0JvKPQQ4hO4vSVVc7M3Vq9drCsGlhEtZl

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-08-11 16:30:29

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 16559)
-- Name: alunos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alunos (
    id_aluno integer NOT NULL,
    nome character varying(100) NOT NULL,
    matricula character varying(20) NOT NULL,
    email character varying(50) NOT NULL,
    curso_id integer
);


ALTER TABLE public.alunos OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16558)
-- Name: alunos_id_aluno_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alunos_id_aluno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.alunos_id_aluno_seq OWNER TO postgres;

--
-- TOC entry 5058 (class 0 OID 0)
-- Dependencies: 225
-- Name: alunos_id_aluno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alunos_id_aluno_seq OWNED BY public.alunos.id_aluno;


--
-- TOC entry 224 (class 1259 OID 16531)
-- Name: cursos_disciplinas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cursos_disciplinas (
    id_curso integer NOT NULL,
    nome_curso character varying(40) NOT NULL,
    codigo character varying(30) NOT NULL,
    disciplina character varying(40) NOT NULL,
    periodo character varying(10) NOT NULL,
    professor_id integer
);


ALTER TABLE public.cursos_disciplinas OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16530)
-- Name: cursos_disciplinas_id_curso_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cursos_disciplinas_id_curso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cursos_disciplinas_id_curso_seq OWNER TO postgres;

--
-- TOC entry 5059 (class 0 OID 0)
-- Dependencies: 223
-- Name: cursos_disciplinas_id_curso_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cursos_disciplinas_id_curso_seq OWNED BY public.cursos_disciplinas.id_curso;


--
-- TOC entry 228 (class 1259 OID 16575)
-- Name: ensalamentos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ensalamentos (
    id_ensalamentos integer NOT NULL,
    curso_id integer,
    sala_id integer,
    professor_id integer,
    data_hora timestamp without time zone NOT NULL
);


ALTER TABLE public.ensalamentos OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16574)
-- Name: ensalamentos_id_ensalamentos_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ensalamentos_id_ensalamentos_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ensalamentos_id_ensalamentos_seq OWNER TO postgres;

--
-- TOC entry 5060 (class 0 OID 0)
-- Dependencies: 227
-- Name: ensalamentos_id_ensalamentos_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ensalamentos_id_ensalamentos_seq OWNED BY public.ensalamentos.id_ensalamentos;


--
-- TOC entry 220 (class 1259 OID 16509)
-- Name: professores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professores (
    id_professor integer NOT NULL,
    nome_professor character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    departamento character varying(100) NOT NULL
);


ALTER TABLE public.professores OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16508)
-- Name: professores_id_professor_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.professores_id_professor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.professores_id_professor_seq OWNER TO postgres;

--
-- TOC entry 5061 (class 0 OID 0)
-- Dependencies: 219
-- Name: professores_id_professor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.professores_id_professor_seq OWNED BY public.professores.id_professor;


--
-- TOC entry 222 (class 1259 OID 16520)
-- Name: salas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.salas (
    id_sala integer NOT NULL,
    numero_sala character varying(50) NOT NULL,
    capacidade integer NOT NULL,
    localizacao character varying(100) NOT NULL
);


ALTER TABLE public.salas OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16519)
-- Name: salas_id_sala_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.salas_id_sala_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.salas_id_sala_seq OWNER TO postgres;

--
-- TOC entry 5062 (class 0 OID 0)
-- Dependencies: 221
-- Name: salas_id_sala_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.salas_id_sala_seq OWNED BY public.salas.id_sala;


--
-- TOC entry 4879 (class 2604 OID 16562)
-- Name: alunos id_aluno; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alunos ALTER COLUMN id_aluno SET DEFAULT nextval('public.alunos_id_aluno_seq'::regclass);


--
-- TOC entry 4878 (class 2604 OID 16534)
-- Name: cursos_disciplinas id_curso; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursos_disciplinas ALTER COLUMN id_curso SET DEFAULT nextval('public.cursos_disciplinas_id_curso_seq'::regclass);


--
-- TOC entry 4880 (class 2604 OID 16578)
-- Name: ensalamentos id_ensalamentos; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamentos ALTER COLUMN id_ensalamentos SET DEFAULT nextval('public.ensalamentos_id_ensalamentos_seq'::regclass);


--
-- TOC entry 4876 (class 2604 OID 16512)
-- Name: professores id_professor; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professores ALTER COLUMN id_professor SET DEFAULT nextval('public.professores_id_professor_seq'::regclass);


--
-- TOC entry 4877 (class 2604 OID 16523)
-- Name: salas id_sala; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salas ALTER COLUMN id_sala SET DEFAULT nextval('public.salas_id_sala_seq'::regclass);


--
-- TOC entry 5050 (class 0 OID 16559)
-- Dependencies: 226
-- Data for Name: alunos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alunos (id_aluno, nome, matricula, email, curso_id) FROM stdin;
1	Felipe Casagrande	202411292	felipe@aluno.edu	1
\.


--
-- TOC entry 5048 (class 0 OID 16531)
-- Dependencies: 224
-- Data for Name: cursos_disciplinas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cursos_disciplinas (id_curso, nome_curso, codigo, disciplina, periodo, professor_id) FROM stdin;
1	Engenharia de Software	ENG101	Banco de Dados	4º Período	1
\.


--
-- TOC entry 5052 (class 0 OID 16575)
-- Dependencies: 228
-- Data for Name: ensalamentos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ensalamentos (id_ensalamentos, curso_id, sala_id, professor_id, data_hora) FROM stdin;
3	1	1	1	2026-08-15 19:00:00
\.


--
-- TOC entry 5044 (class 0 OID 16509)
-- Dependencies: 220
-- Data for Name: professores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.professores (id_professor, nome_professor, email, departamento) FROM stdin;
1	Diego	zedacouve@faculdade.edu	Computação
\.


--
-- TOC entry 5046 (class 0 OID 16520)
-- Dependencies: 222
-- Data for Name: salas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.salas (id_sala, numero_sala, capacidade, localizacao) FROM stdin;
1	Bloco A - 101	40	Prédio Principal
2	Bloco B - 203	30	Prédio Novo
\.


--
-- TOC entry 5063 (class 0 OID 0)
-- Dependencies: 225
-- Name: alunos_id_aluno_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alunos_id_aluno_seq', 1, true);


--
-- TOC entry 5064 (class 0 OID 0)
-- Dependencies: 223
-- Name: cursos_disciplinas_id_curso_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cursos_disciplinas_id_curso_seq', 1, true);


--
-- TOC entry 5065 (class 0 OID 0)
-- Dependencies: 227
-- Name: ensalamentos_id_ensalamentos_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ensalamentos_id_ensalamentos_seq', 3, true);


--
-- TOC entry 5066 (class 0 OID 0)
-- Dependencies: 219
-- Name: professores_id_professor_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.professores_id_professor_seq', 1, false);


--
-- TOC entry 5067 (class 0 OID 0)
-- Dependencies: 221
-- Name: salas_id_sala_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.salas_id_sala_seq', 2, true);


--
-- TOC entry 4888 (class 2606 OID 16568)
-- Name: alunos alunos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_pkey PRIMARY KEY (id_aluno);


--
-- TOC entry 4886 (class 2606 OID 16541)
-- Name: cursos_disciplinas cursos_disciplinas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursos_disciplinas
    ADD CONSTRAINT cursos_disciplinas_pkey PRIMARY KEY (id_curso);


--
-- TOC entry 4890 (class 2606 OID 16582)
-- Name: ensalamentos ensalamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamentos
    ADD CONSTRAINT ensalamentos_pkey PRIMARY KEY (id_ensalamentos);


--
-- TOC entry 4882 (class 2606 OID 16518)
-- Name: professores professores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professores
    ADD CONSTRAINT professores_pkey PRIMARY KEY (id_professor);


--
-- TOC entry 4884 (class 2606 OID 16529)
-- Name: salas salas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_pkey PRIMARY KEY (id_sala);


--
-- TOC entry 4892 (class 2606 OID 16569)
-- Name: alunos alunos_curso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_curso_id_fkey FOREIGN KEY (curso_id) REFERENCES public.cursos_disciplinas(id_curso);


--
-- TOC entry 4891 (class 2606 OID 16542)
-- Name: cursos_disciplinas cursos_disciplinas_professor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursos_disciplinas
    ADD CONSTRAINT cursos_disciplinas_professor_id_fkey FOREIGN KEY (professor_id) REFERENCES public.professores(id_professor);


--
-- TOC entry 4893 (class 2606 OID 16583)
-- Name: ensalamentos ensalamentos_curso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamentos
    ADD CONSTRAINT ensalamentos_curso_id_fkey FOREIGN KEY (curso_id) REFERENCES public.cursos_disciplinas(id_curso);


--
-- TOC entry 4894 (class 2606 OID 16593)
-- Name: ensalamentos ensalamentos_professor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamentos
    ADD CONSTRAINT ensalamentos_professor_id_fkey FOREIGN KEY (professor_id) REFERENCES public.professores(id_professor);


--
-- TOC entry 4895 (class 2606 OID 16588)
-- Name: ensalamentos ensalamentos_sala_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamentos
    ADD CONSTRAINT ensalamentos_sala_id_fkey FOREIGN KEY (sala_id) REFERENCES public.salas(id_sala);


-- Completed on 2026-08-11 16:30:29

--
-- PostgreSQL database dump complete
--

\unrestrict zYTY0NrCR41eKxIiCvsjPW2Ii5hBkL0JvKPQQ4hO4vSVVc7M3Vq9drCsGlhEtZl

