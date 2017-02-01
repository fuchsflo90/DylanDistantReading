import java.util.ArrayList;

public class Songs {
	// Metadaten
		private String parlamentsname;
		private String sitzungsnummer;
		private String regierungsperiode;
		private String zeitraum;
		private String originaldatei;
		// Stimmungsannotationen Liste
		private ArrayList<Song> songs;

		public Songs() {
			songs = new ArrayList<Song>();
		}

		public void speichereMetadaten(String parlamentsname,
				String sitzungsnummer, String regierungsperiode, String zeitraum,
				String originaldatei) {

			this.parlamentsname = parlamentsname;
			this.sitzungsnummer = sitzungsnummer;
			this.regierungsperiode = regierungsperiode;
			this.zeitraum = zeitraum;
			this.originaldatei = originaldatei;

			if (Configurations.debugMetaInfo) {
				System.out.println("_____________________Metainformationen...");
				System.out.println("_____________________|_____________________ "
						+ parlamentsname);
				System.out.println("_____________________|_____________________ "
						+ sitzungsnummer + ". Sitzung der " + regierungsperiode
						+ ". Gesetzgebungsperiode");
				System.out.println("_____________________|_____________________ "
						+ "am " + zeitraum);
				System.out.println("_____________________|_____________________ "
						+ "Datei: " + originaldatei);
			}
		}

		public void newSong(String title, String text, String date, String album, String author){
			int songId = songs.size()+1;
			songs.add(new Song(songId, title, text, date, album, author));
		}
		
		public String gebeParlamentsname() {
			return parlamentsname;
		}

		public String gebeSitzungsnummer() {
			return sitzungsnummer;
		}

		public String gebeRegierungsperiode() {
			return regierungsperiode;
		}

		public String gebeZeitraum() {
			return zeitraum;
		}

		public String gebeOriginalDateifad() {
			return originaldatei;
		}

		public int getNumberOfSongs() {
			return songs.size();
		}
		
		public int getId(int i){
			return songs.get(i).getId();
		}
		
		public String getTitle(int i){
			return songs.get(i).getTitle();
		}
		
		public String getText(int i){
			return songs.get(i).getText();
		}
		public String getDate(int i){
			return songs.get(i).getDate();
		}
		
		public String getAlbum(int i){
			return songs.get(i).getAlbum();
		}
		
		public String getAuthor(int i){
			return songs.get(i).getAuthor();
		}
		
		
		class Song {
			
			int id;
			String title;
			String text;
			String date;
			String album;
			String author;
			
			Song (int id, String title, String text, String date, String album, String author){
				this.id = id;
				this.title = title;
				this.text = text;
				this.date = date;
				this.album = album;
				this.author = author;
			}
			
			int getId(){
				return id;
			}
			String getTitle(){
				return title;
			}
			String getText(){
				return text;
			}
			String getDate(){
				return date;
			}
			String getAlbum(){
				return album;
			}
			String getAuthor(){
				return author;
			}
		}
}
