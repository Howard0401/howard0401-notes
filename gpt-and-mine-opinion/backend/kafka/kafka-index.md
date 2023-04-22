
# kafka 3.4.0

1. AbstractIndex:

```scala
/**
 * @param _file The index file
 * @param baseOffset the base offset of the segment that this index is corresponding to.
 * @param maxIndexSize The maximum index size in bytes.
 */
  // init class cosntructor
  abstract class AbstractIndex(@volatile private var _file: File, val baseOffset: Long, val maxIndexSize: Int = -1,
                             val writable: Boolean) extends Closeable

  // exist or null
  private volatile File file;
  // Length of the index file
  private var _length: Long = _

  // Offset Index override def entrySize = 8
  // Time Index override def entrySize = 12
  protected def entrySize: Int
 
  /*
   We can't set make N (_warmEntries) to be larger than 8192, as there is no simple way to guarantee all the "warm"
   section pages are really warm (touched in every lookup) on a typical 4KB-page host.
   1. When doing warm-section lookup, following 3 entries are always touched: indexEntry(end), indexEntry(end-N),
      and indexEntry((end*2 -N)/2). If page size >= 4096, all the warm-section pages (3 or fewer) are touched, when we
      touch those 3 entries. As of 2018, 4096 is the smallest page size for all the processors (x86-32, x86-64, MIPS,
      SPARC, Power, ARM etc.).
   2. This number is large enough to guarantee most of the in-sync lookups are in the warm-section. With default Kafka
      settings, 8KB index corresponds to about 4MB (offset index) or 2.7MB (time index) log messages.
  */
  // The warm entries should be no more than 3 pages.
  protected def _warmEntries: Int = 8192 / entrySize

  // Tread Lock
  protected val lock = new ReentrantLock

  // *** write data to channel, this is the most important part, // 重點
  // Kafka store bytes into a map per NIO thread
  protected var mmap: MappedByteBuffe

  // no more slots available in this index
  def isFull: Boolean = _entries >= _maxEntries
  def file: File = _file
  // The maximum number of entries this index can hold
  def maxEntries: Int = _maxEntries // = mmap.limit() / entrySize
  // The number of entries in this index
  def entries: Int = _entries // = mmap.position() / entrySize
  def length: Long = _length
  def updateParentDir(parentDir: File): Unit
  // Reset the size of the memory map and the underneath file
  // 1. trimToValidSize()
  // 2. loading segments from disk or truncating back to an old segment where a new log segment became active
  def resize(newSize: Int): Boolean

  def renameTo(f: File): Unit

  // force restore file
  def flush(): Unit 

  def deleteIfExists(): Boolean

  // The number of bytes actually used by this index
  def sizeInBytes: Int = entrySize * _entries

  //  close index 1. trimToValidSize 2. closeHandler
  def close(): Unit
  // prevent application threads(STW) for a long moment reading metadata from a physical disk.
  def closeHandler(): Unit

  def sanityCheck(): Unit

  // Remove all the entries from the index.
  protected def truncate(): Unit
  def truncateTo(offset: Long): Unit
  // 1. truncate 2. resize(maxIndexSize)
  def reset(): Unit

  // get offset relative to base offset of this index
  def relativeOffset(offset: Long): Int
  // check offset is valid
  def canAppendOffset(offset: Long): Boolean

  // delete mmap
  protected[log] def forceUnmap(): Unit

  // Windows and ZOS cannot resize, so we need to lock it
  protected def maybeLock[T](lock: Lock)(fun: => T): T 

  // get index entry
  protected def parseEntry(buffer: ByteBuffer, n: Int): IndexEntry
  // For offsetIndex, TimeIndex, lookup and truncateTo, find the slot in which the largest entry less than or equal to the given target key or value is stored.
  protected def largestLowerBoundSlotFor(idx: ByteBuffer, target: Long, searchEntity: IndexSearchType): Int
  // for offsetIndex fetchUpperBoundOffset, generally is  used to find the offset from the start index to the upper bound.
  protected def smallestUpperBoundSlotFor(idx: ByteBuffer, target: Long, searchEntity: IndexSearchType): Int
  // binary search is performed using _warmEntries (less than 3 pages) if possible, otherwise it is performed without _warmEntries. like LRU
  private def indexSlotRangeFor(idx: ByteBuffer, target: Long, searchEntity: IndexSearchType): (Int, Int)
  // search key or value
  private def compareIndexEntry(indexEntry: IndexEntry, target: Long, searchEntity: IndexSearchType): Int

  // Round a number to the greatest exact multiple of the given factor less than the given number.
  private def roundDownToExactMultiple(number: Int, factor: Int) = factor * (number / factor)
  private def toRelative(offset: Long): Option[Int]


```


2. OffsetIndex


```scala
  class OffsetIndex(_file: File, baseOffset: Long, maxIndexSize: Int = -1, writable: Boolean = true)
    extends AbstractIndex(_file, baseOffset, maxIndexSize, writable)

  private def lastEntry: OffsetPosition

  def lastOffset: Long = _lastOffset
```



4. LazyIndex

 * [From doc] This is an important optimization with regards to broker start-up and shutdown time, if it has a large number of segments.
 * Initialize the index using abstrct class for a wrapped index, and then call it with a lock while considering thread safety.
 * 即初始化時包裝索引並加鎖，使用後解鎖，達到不用主動取得 init 的 index.


```scala
  // lock
  private val lock = new ReentrantLock()
  def file: File

  // From IndexWrapper
  def updateParentDir(parentDir: File): Unit
  def renameTo(f: File): Unit
  def deleteIfExists(): Boolean
  def close()
  def closeHandler(): Unit
```

`implement`
```java
  public static class IndexFile
  public static class IndexValue<T>
```

