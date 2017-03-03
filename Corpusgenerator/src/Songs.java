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
			title = title.replaceAll("\\n", "");
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
		
		public boolean isInList(String title){
			
			title = title.toLowerCase();
			
			for (int i=0; i < songs.size(); i++){
				
				
				if (songs.get(i).title.toLowerCase().contains(title) ){
					System.out.println("DUPLIKAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111einseinself");
					return true;
				}
			}
			
			return false;
		}
		
		private class Song {
			
			private int id;
			private String title;
			private String text;
			private String date;
			private String album;
			private String author;
			private String filePath;
			
			public Song (int id, String title, String text, String date, String album, String author, String filePath){
				this.id = id;
				this.title = title;
				this.text = text;
				this.date = date;
				this.album = album;
				this.author = author;
				this.filePath = filePath;
				
				this.title = title.toLowerCase();
				
				if (this.title.contains("california")){
					this.date = "1965";
				}
				
				if (this.title.contains("do re mi")){
					this.date = "2009";
				}
				
				if (this.title.contains("don't ever take yourself away")){
					this.date = "1999";
				}
				
				if (this.title.contains("freedom for the stallion")){
					this.date = "1984";
				}
				
				if (this.title.contains("guess things happen that way (studio outtake)")){
					this.date = "1969";
				}
				
				if (this.title.contains("hallelujah")){
					this.date = "1999";
				}
				
				if (this.title.contains("lost highway")){
					this.date = "1965";
				}
				
				if (this.title.contains("playboys and playgirls")){
					this.date = "1964";
				}
				
				if (this.title.contains("red cadillac and a black moustache")){
					this.date = "2001";
				}
				
				if (this.title.contains("roving gambler")){
					this.date = "1991";
				}
				
				if (this.title.contains("that's alright mama")){
					this.date = "1995";
				}
				
				if (this.title.contains("train a-travelin'")){
					this.date = "1962";
				}
				
				if (this.title.contains("waiting for you")){
					this.date = "2002";
				}
				
				if (this.title.contains("workingman's blues #2 (live)")){
					this.date = "2070";
				}
				
				if (this.title.contains("you belong to me")){
					this.date = "1994";
				}
				//System.out.println(this.title + ";" + this.date); 
			}
			
			public int getId(){
				return this.id;
			}
			public String getTitle(){
				return this.title;
			}
			public String getText(){
				return this.text;
			}
			public String getDate(){
				return this.date;
			}
			public String getAlbum(){
				return this.album;
			}
			public String getAuthor(){
				return this.author;
			}
			public String getFilePath(){
				return this.filePath;
			}
		}
}
