import java.util.ArrayList;

public class Songs {
	// Metadaten
		private String originaldatei;
		// Stimmungsannotationen Liste
		private ArrayList<Song> songs;

		public Songs() {
			songs = new ArrayList<Song>();
		}

		public void newSong(String title, String text, String date, String album, String author, String filePath){
			int songId = songs.size()+1;
			songs.add(new Song(songId, title, text, date, album, author, filePath));
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
		
		public String getFilePath(int i){
			return songs.get(i).getFilePath();
		}
		
		
		class Song {
			
			int id;
			String title;
			String text;
			String date;
			String album;
			String author;
			String filePath;
			
			Song (int id, String title, String text, String date, String album, String author, String filePath){
				this.id = id;
				this.title = title;
				this.text = text;
				this.date = date;
				this.album = album;
				this.author = author;
				this.filePath = filePath;
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
			String getFilePath(){
				return filePath;
			}
		}
}
