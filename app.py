import streamlit as st
import sqlite3
from datetime import datetime

# Page configuration
st.set_page_config(page_title="🏛️ Luxe Hôtel", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            color: #1e3a8a;
        }
        .main {
            background: #ffffff;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            padding: 2rem;
            margin: 2rem auto;
            max-width: 1200px;
        }
        h1 {
            color: #d4af37;
            text-align: center;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #1e3a8a;
            font-weight: 600;
            font-size: 1.8rem;
            margin-top: 1.5rem;
        }
        .stButton button {
            background: linear-gradient(45deg, #d4af37, #b8972e);
            color: #ffffff;
            font-size: 1.1rem;
            font-weight: 600;
            border: none;
            border-radius: 25px;
            padding: 0.8rem 1.5rem;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        .stButton button.reset-button {
            background: linear-gradient(45deg, #6b7280, #4b5563);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        .stButton button.reset-button:hover {
            background: linear-gradient(45deg, #4b5563, #6b7280);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }
        .stTextInput, .stSelectbox, .stDateInput {
            background: white;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            padding: 0.5rem;
            transition: border-color 0.2s;
        }
        .stTextInput:focus, .stSelectbox:focus, .stDateInput:focus {
            border-color: #d4af37;
        }
        .card {
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
            display: block !important; /* Ensure cards are visible */
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .info-box {
            background: #e6f0fa;
            border-left: 5px solid #3b82f6;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            font-size: 1rem;
            color: #1e3a8a;
        }
        .success-box {
            background: #d1fae5;
            border-left: 5px solid #10b981;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            font-size: 1rem;
            color: #065f46;
        }
        .warning-box {
            background: #fef3c7;
            border-left: 5px solid #f59e0b;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            font-size: 1rem;
            color: #92400e;
        }
        hr {
            border: 0;
            height: 2px;
            background: linear-gradient(to right, transparent, #d4af37, transparent);
            margin: 1.5rem 0;
        }
        .menu-buttons {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }
        @media (max-width: 768px) {
            .main {
                margin: 1rem;
                padding: 1rem;
            }
            h1 {
                font-size: 2rem;
            }
            .stButton button {
                font-size: 1rem;
                padding: 0.6rem 1.2rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Database connection
def get_db_connection():
    conn = sqlite3.connect("hotel_management.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# Initialize session state
if "addClient" not in st.session_state:
    st.session_state.addClient = False
if "addRes" not in st.session_state:
    st.session_state.addRes = False
if "showReservations" not in st.session_state:
    st.session_state.showReservations = False
if "showClients" not in st.session_state:
    st.session_state.showClients = False
if "showAvailableRooms" not in st.session_state:
    st.session_state.showAvailableRooms = False
if "showEvaluations" not in st.session_state:
    st.session_state.showEvaluations = False

# Navigation functions
def reset_to_menu():
    st.session_state.addClient = False
    st.session_state.addRes = False
    st.session_state.showReservations = False
    st.session_state.showClients = False
    st.session_state.showAvailableRooms = False
    st.session_state.showEvaluations = False

def show_client_form():
    st.session_state.addClient = True
    reset_to_menu()
    st.session_state.addClient = True

def show_reservation_form():
    st.session_state.addRes = True
    reset_to_menu()
    st.session_state.addRes = True

def show_reservations():
    st.session_state.showReservations = True
    reset_to_menu()
    st.session_state.showReservations = True

def show_clients():
    st.session_state.showClients = True
    reset_to_menu()
    st.session_state.showClients = True

def show_available_rooms():
    st.session_state.showAvailableRooms = True
    reset_to_menu()
    st.session_state.showAvailableRooms = True

def show_evaluations():
    st.session_state.showEvaluations = True
    reset_to_menu()
    st.session_state.showEvaluations = True

# Main title
st.markdown("<h1><i class='fas fa-hotel'></i> Luxe Hôtel Management</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Main menu
with st.container():
    st.markdown("<div class='menu-buttons'>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.button("📋 Réservations", on_click=show_reservations)
    with col2:
        st.button("👥 Clients", on_click=show_clients)
    with col3:
        st.button("🛏️ Chambres", on_click=show_available_rooms)
    with col4:
        st.button("➕ Nouveau Client", on_click=show_client_form)
    with col5:
        st.button("🗓️ Nouvelle Réservation", on_click=show_reservation_form)
    with col6:
        st.button("📝 Évaluations", on_click=show_evaluations)
    st.markdown("</div>", unsafe_allow_html=True)

# List reservations
if st.session_state.showReservations:
    st.markdown("<h2><i class='fas fa-list'></i> Liste des Réservations</h2>", unsafe_allow_html=True)
    conn = get_db_connection()
    reservations = conn.execute("""
        SELECT r.idRéservation, c.nom, h.ville, r.dateArrivée, r.dateDépart
        FROM Réservation r
        JOIN Client c ON r.idClient = c.idClient
        JOIN Chambre ch ON r.idChambre = ch.idChambre
        JOIN Hotel h ON ch.idHotel = h.idHotel
    """).fetchall()
    conn.close()
    
    st.write("Debug: Found", len(reservations), "reservations")
    if reservations:
        for res in reservations:
            st.markdown(f"""
                <div class='card'>
                    <strong>Réservation #{res['idRéservation']}</strong>: {res['nom']} à {res['ville']}<br>
                    <i class='fas fa-calendar-alt'></i> {res['dateArrivée']} au {res['dateDépart']}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<div class='info-box'><i class='fas fa-info-circle'></i> Aucune réservation trouvée.</div>", unsafe_allow_html=True)
    
    st.button("↩️ Retour au Menu", on_click=reset_to_menu, help="Retourner au menu principal")

# List clients
if st.session_state.showClients:
    st.markdown("<h2><i class='fas fa-users'></i> Liste des Clients</h2>", unsafe_allow_html=True)
    conn = get_db_connection()
    clients = conn.execute("SELECT nom, ville, email, telephone FROM Client").fetchall()
    conn.close()
    
    st.write("Debug: Found", len(clients), "clients")
    if clients:
        for client in clients:
            st.markdown(f"""
                <div class='card'>
                    <strong>{client['nom']}</strong> ({client['ville']})<br>
                    <i class='fas fa-envelope'></i> {client['email']} | <i class='fas fa-phone'></i> {client['telephone']}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<div class='info-box'><i class='fas fa-info-circle'></i> Aucun client trouvé.</div>", unsafe_allow_html=True)
    
    st.button("↩️ Retour au Menu", on_click=reset_to_menu, help="Retourner au menu principal")

# Available rooms
if st.session_state.showAvailableRooms:
    st.markdown("<h2><i class='fas fa-bed'></i> Chambres Disponibles</h2>", unsafe_allow_html=True)
    
    with st.form("available_rooms_form"):
        col1, col2 = st.columns(2)
        with col1:
            date_start = st.date_input("📅 Date de début")
        with col2:
            date_end = st.date_input("📅 Date de fin")
        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            submitted = st.form_submit_button("🔍 Vérifier Disponibilité")
        with col_reset:
            st.form_submit_button("↩️ Retour au Menu", on_click=reset_to_menu)
        
        if submitted:
            if date_end <= date_start:
                st.markdown("<div class='warning-box'><i class='fas fa-exclamation-triangle'></i> La date de fin doit être postérieure à la date de début.</div>", unsafe_allow_html=True)
            else:
                conn = get_db_connection()
                rooms = conn.execute("""
                    SELECT ch.idChambre, ch.numero, h.ville, tc.libellé
                    FROM Chambre ch
                    JOIN Hotel h ON ch.idHotel = h.idHotel
                    JOIN TypeChambre tc ON ch.idTypeChambre = tc.idTypeChambre
                    WHERE ch.idChambre NOT IN (
                        SELECT r.idChambre
                        FROM Réservation r
                        WHERE r.dateArrivée <= ? AND r.dateDépart >= ?
                    )
                """, (date_end.strftime('%Y-%m-%d'), date_start.strftime('%Y-%m-%d'))).fetchall()
                conn.close()
                
                st.write("Debug: Found", len(rooms), "available rooms")
                if rooms:
                    for room in rooms:
                        st.markdown(f"""
                            <div class='card'>
                                <strong>Chambre {room['numero']}</strong> ({room['libellé']})<br>
                                <i class='fas fa-map-marker-alt'></i> {room['ville']}
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("<div class='info-box'><i class='fas fa-info-circle'></i> Aucune chambre disponible pour cette période.</div>", unsafe_allow_html=True)

# List evaluations
if st.session_state.showEvaluations:
    st.markdown("<h2><i class='fas fa-star'></i> Liste des Évaluations</h2>", unsafe_allow_html=True)
    conn = get_db_connection()
    evaluations = conn.execute("""
        SELECT e.idÉvaluation, c.nom, e.dateÉvaluation, e.note, e.commentaire
        FROM Évaluation e
        JOIN Client c ON e.idClient = c.idClient
    """).fetchall()
    conn.close()
    
    st.write("Debug: Found", len(evaluations), "evaluations")
    if evaluations:
        for eval in evaluations:
            st.markdown(f"""
                <div class='card'>
                    <strong>Évaluation #{eval['idÉvaluation']}</strong> par {eval['nom']}<br>
                    <i class='fas fa-calendar-alt'></i> {eval['dateÉvaluation']} | 
                    <i class='fas fa-star'></i> Note: {eval['note']}/5<br>
                    <i class='fas fa-comment'></i> {eval['commentaire'] or 'Aucun commentaire'}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<div class='info-box'><i class='fas fa-info-circle'></i> Aucune évaluation trouvée.</div>", unsafe_allow_html=True)
    
    st.button("↩️ Retour au Menu", on_click=reset_to_menu, help="Retourner au menu principal")

# Add client form
if st.session_state.addClient:
    st.markdown("<h2><i class='fas fa-user-plus'></i> Ajouter un Client</h2>", unsafe_allow_html=True)
    
    with st.form("form_ajout_client", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            cin = st.text_input("🆔 CIN", placeholder="Entrez le CIN")
            nom = st.text_input("👤 Nom Complet", placeholder="Entrez le nom")
            code_postal = st.text_input("📮 Code Postal", placeholder="Entrez le code postal")
        with col2:
            ville = st.selectbox("🏙️ Ville", [
                "Paris", "Lyon", "Marseille", "Lille", "Nice"
            ], placeholder="Sélectionnez une ville")
            email = st.text_input("📧 Email", placeholder="Entrez l'email")
            telephone = st.text_input("📱 Téléphone", placeholder="Entrez le téléphone")
        adresse = st.text_input("🏠 Adresse", placeholder="Entrez l'adresse")
        
        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            submitted = st.form_submit_button("✅ Enregistrer le Client")
        with col_reset:
            st.form_submit_button("↩️ Retour au Menu", on_click=reset_to_menu)
        
        if submitted:
            missing_fields = []
            if not cin:
                missing_fields.append("CIN")
            if not nom:
                missing_fields.append("Nom")
            if not adresse:
                missing_fields.append("Adresse")
            if not ville:
                missing_fields.append("Ville")
            if not code_postal:
                missing_fields.append("Code Postal")
            if not email:
                missing_fields.append("Email")
            if not telephone:
                missing_fields.append("Téléphone")
            
            if missing_fields:
                st.markdown(f"<div class='warning-box'><i class='fas fa-exclamation-triangle'></i> Veuillez remplir les champs suivants : {', '.join(missing_fields)}.</div>", unsafe_allow_html=True)
            else:
                conn = get_db_connection()
                cursor = conn.cursor()
                try:
                    cursor.execute("""
                        INSERT INTO Client (idClient, adresse, ville, codePostal, email, telephone, nom)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (cin, adresse, ville, code_postal, email, telephone, nom))
                    conn.commit()
                    st.markdown("<div class='success-box'><i class='fas fa-check-circle'></i> Client enregistré avec succès !</div>", unsafe_allow_html=True)
                except sqlite3.IntegrityError:
                    st.markdown("<div class='warning-box'><i class='fas fa-exclamation-triangle'></i> Erreur : CIN déjà utilisé ou données invalides.</div>", unsafe_allow_html=True)
                finally:
                    conn.close()

# Add reservation form
if st.session_state.addRes:
    st.markdown("<h2><i class='fas fa-calendar-plus'></i> Ajouter une Réservation</h2>", unsafe_allow_html=True)
    
    with st.form("form_ajout_res", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            dateArr = st.date_input("📅 Date d'Arrivée")
        with col2:
            dateDep = st.date_input("📅 Date de Départ")
        cin = st.text_input("🔑 CIN du Client", placeholder="Entrez le CIN")
        
        conn = get_db_connection()
        rooms = conn.execute("""
            SELECT ch.idChambre, ch.numero, h.ville, tc.libellé
            FROM Chambre ch
            JOIN Hotel h ON ch.idHotel = h.idHotel
            JOIN TypeChambre tc ON ch.idTypeChambre = tc.idTypeChambre
        """).fetchall()
        room_options = [f"Chambre {r['numero']} ({r['libellé']}, {r['ville']})" for r in rooms]
        selected_room = st.selectbox("🛏️ Chambre", room_options, placeholder="Sélectionnez une chambre")
        room_id = rooms[room_options.index(selected_room)]['idChambre'] if room_options and selected_room else None
        conn.close()

        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            submitted_res = st.form_submit_button("✅ Enregistrer la Réservation")
        with col_reset:
            st.form_submit_button("↩️ Retour au Menu", on_click=reset_to_menu)
        
        if submitted_res:
            errors = []
            if not cin:
                errors.append("CIN du client est requis")
            if not selected_room:
                errors.append("Aucune chambre sélectionnée")
            if dateDep <= dateArr:
                errors.append("La date de départ doit être postérieure à la date d'arrivée")
            
            if errors:
                st.markdown(f"<div class='warning-box'><i class='fas fa-exclamation-triangle'></i> Erreurs : {'; '.join(errors)}.</div>", unsafe_allow_html=True)
            else:
                conn = get_db_connection()
                cursor = conn.cursor()
                client = cursor.execute("SELECT idClient FROM Client WHERE idClient = ?", (cin,)).fetchone()
                if not client:
                    st.markdown("<div class='warning-box'><i class='fas fa-exclamation-triangle'></i> Client non trouvé.</div>", unsafe_allow_html=True)
                else:
                    conflict = cursor.execute("""
                        SELECT idRéservation FROM Réservation
                        WHERE idChambre = ? AND dateArrivée <= ? AND dateDépart >= ?
                    """, (room_id, dateDep.strftime('%Y-%m-%d'), dateArr.strftime('%Y-%m-%d'))).fetchone()
                    if conflict:
                        st.markdown("<div class='warning-box'><i class='fas fa-exclamation-triangle'></i> Cette chambre est déjà réservée pour la période sélectionnée.</div>", unsafe_allow_html=True)
                    else:
                        try:
                            cursor.execute("""
                                INSERT INTO Réservation (idRéservation, dateArrivée, dateDépart, idClient, idChambre)
                                VALUES ((SELECT COALESCE(MAX(idRéservation), 0) + 1 FROM Réservation), ?, ?, ?, ?)
                            """, (dateArr.strftime('%Y-%m-%d'), dateDep.strftime('%Y-%m-%d'), cin, room_id))
                            conn.commit()
                            st.markdown("<div class='success-box'><i class='fas fa-check-circle'></i> Réservation enregistrée avec succès !</div>", unsafe_allow_html=True)
                        except sqlite3.IntegrityError:
                            st.markdown("<div class='warning-box'><i class='fas fa-exclamation-triangle'></i> Erreur lors de l'enregistrement de la réservation.</div>", unsafe_allow_html=True)
                conn.close()
